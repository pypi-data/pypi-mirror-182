def main():
    """

    Function to print the instructions to set the environment variable HDF5_PLUGIN_PATH.

    """

    import hdf5plugin
    from pathlib import Path
    hdf5plugin_folder = Path(hdf5plugin.__file__).parent
    plugins_folder = hdf5plugin_folder / "plugins"
    print(f"export HDF5_PLUGIN_PATH={plugins_folder.as_posix()}")


if __name__ == "__main__":
    main()
