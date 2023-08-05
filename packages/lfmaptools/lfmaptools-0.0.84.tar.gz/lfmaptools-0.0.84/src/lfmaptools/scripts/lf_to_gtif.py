import ast
import os
import pathlib
import tempfile
import zipfile

import click
import rioxarray as rxr
import xarray as xr

from lfmaptools.netcdf_utils import lfnc
from lfmaptools.textfile_utils import lftxt
from lfmaptools.utilities import _path_of_file_in_zip


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


class PathPath(click.Path):
    """A Click path argument that returns a pathlib Path, not a string"""

    def convert(self, value, param, ctx):
        return pathlib.Path(super().convert(value, param, ctx))


@click.command()
@click.argument(
    "src",
    type=PathPath(
        exists=True,
        file_okay=True,
        dir_okay=True,
        writable=False,
        readable=True,
    ),
)
@click.argument(
    "input_file",
    type=PathPath(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
    ),
)
@click.option(
    "-dest",
    "--dest",
    "dest",
    type=PathPath(
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
    ),
    prompt="Set destination directory",
    default=os.getcwd(),
)
@click.option(
    "-o",
    "--out_filename",
    "file_out",
    type=click.File(mode="w"),
    is_flag=False,
    flag_value=None,
)
@click.option(
    "-v",
    "--var",
    "var",
    type=click.STRING,
    multiple=True,
)
def lf_to_gtif(src, input_file, dest, file_out, var):

    if file_out is None:
        file_out = input_file.with_suffix(".tif")

    if src.is_dir():
        zipped = False
    else:
        if src.suffix == ".zip":
            zipped = True
        else:
            raise ValueError(
                f"Input directory {src} neither a LaharFlow zip file nor a directory"
            )

    if len(var) == 0:
        var = None
    else:
        if type(var) is tuple:
            var = list(var)
        # var = [var]

    if zipped:
        tmpdirname = tempfile.TemporaryDirectory()
        zipref = zipfile.ZipFile(src, "r")
        infoFilePath = _path_of_file_in_zip("RunInfo.txt", zipref)[0]
        zipref.extract(infoFilePath, tmpdirname.name)
        resultFilePath = _path_of_file_in_zip(input_file.name, zipref)[0]
        zipref.extract(resultFilePath, tmpdirname.name)
        zipref.close()
        dir = tmpdirname.name
    else:
        dir = src
        resultFilePath = input_file

    result_file = os.path.join(dir, resultFilePath)
    result_file_ext = pathlib.Path(result_file).suffix

    if result_file_ext == ".nc":
        data = lfnc(result_file)
    elif result_file_ext == ".txt":
        info_file = os.path.join(dir, "RunInfo.txt")
        data = lftxt(result_file, info_file)
    else:
        raise RuntimeError("result file not recognized")

    raster = data.to_xarray(vars=var)

    fileOut = os.path.join(dest.resolve(), file_out.name)

    print("Writing file to {}".format(fileOut))
    raster.rio.to_raster(fileOut)

    if zipped:
        tmpdirname.cleanup()
