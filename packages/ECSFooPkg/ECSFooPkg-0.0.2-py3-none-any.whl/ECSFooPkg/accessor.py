from os import PathLike
from typing import Union

import xarray
import hdf5plugin  # noqa
from enstools.encoding.api import FilterEncodingForXarray


@xarray.register_dataset_accessor("to_compressed_netcdf")
class ToCompressedNetcdf:
    def __init__(self, xarray_obj: xarray.Dataset):
        """
        Initialize the accessor saving a reference of the dataset.

        Parameters
        ----------
        xarray_obj: xarray.Dataset
        """
        self._obj = xarray_obj

    def __call__(self, path: Union[str, PathLike, None] = None, compression: str = None, **kwargs) -> \
            Union[bytes, None]:
        """
        The accessor is a shortcut to to_netcdf adding the proper encoding and the engine arguments.

        Parameters
        ----------
        path: str | pathlike | None
        compression: str
        kwargs: Any other keyword arguments that can be used with xarray's to_netcdf method.

        Returns
        -------

        """

        encoding = FilterEncodingForXarray(self._obj, compression=compression)
        encoding.add_metadata()
        return self._obj.to_netcdf(path, encoding=encoding, engine="h5netcdf", **kwargs)
