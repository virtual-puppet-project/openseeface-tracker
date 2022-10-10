import os
import platform
import shutil
import requests
import tarfile

WINDOWS: str = "windows"
LINUX: str = "linux"
OSX: str = "osx"

OSF_TAR_NAME: str = "OpenSeeFace.tar.gz"
OSF_DIR_NAME: str = "OpenSeeFace"


def setup(args: dict) -> None:
    print("Setting up openseeface-tracker")

    if not os.path.isdir(OSF_DIR_NAME):
        # Cleanup tar file if it already exists, otherwise things might be very subtly broken
        if os.path.isdir(OSF_TAR_NAME):
            shutil.rmtree(OSF_TAR_NAME)

        os_name: str = ""
        if args.os == "windows":
            os_name = "windows"
        elif args.os == "linux":
            os_name = "linux"
        elif args.os == "osx":
            os_name = "mac"
        else:
            raise Exception("Unhandled os: {}".format(args.os))

        print("Downloading OpenSeeFace binary", flush=True)
        # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
        with requests.get(
                "https://github.com/you-win/OpenSeeFace/releases/download/latest/OpenSeeFace_latest_{}.tar.gz".format(os_name), stream=True) as r:
            with open(OSF_TAR_NAME, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        print("Finished downloading OpenSeeFace binary", flush=True)

        print("Decompressing tar.gz")
        with tarfile.open(OSF_TAR_NAME, "r:gz") as f:
            f.extractall()

        print("Deleting tar.gz")
        os.remove(OSF_TAR_NAME)

        print("Creating .gdignore")
        open("{}/.gdignore".format(OSF_DIR_NAME), "a").close()

    if args.export:
        shutil.rmtree(".github")
        if os.path.isdir("__pycache__"):
            shutil.rmtree("__pycache__")

    print("Finished setting up openseeface-tracker")


def clean(_args: dict) -> None:
    if os.path.isdir(OSF_TAR_NAME):
        shutil.rmtree(OSF_TAR_NAME)
    if os.path.isdir(OSF_DIR_NAME):
        shutil.rmtree(OSF_DIR_NAME)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    from argparse import ArgumentParser

    parser = ArgumentParser()

    subparsers = parser.add_subparsers()

    setup_parser = subparsers.add_parser("setup")
    setup_parser.add_argument(
        "--os", choices=["windows", "linux", "osx"], default="")
    setup_parser.add_argument("--no-pyinstaller", action="store_true")
    setup_parser.add_argument("--export", action="store_true")
    setup_parser.set_defaults(func=setup)

    clean_parser = subparsers.add_parser("clean")
    clean_parser.set_defaults(func=clean)

    args = parser.parse_args()

    if not args.os:
        args.os = platform.system()
        if args.os == "Windows":
            args.os = WINDOWS
        elif args.os == "Linux":
            args.os = LINUX
        elif args.os == "Darwin":
            args.os = OSX
        else:
            raise Exception("Unhandled OS: {}".format(args.os))

    args.func(args)
