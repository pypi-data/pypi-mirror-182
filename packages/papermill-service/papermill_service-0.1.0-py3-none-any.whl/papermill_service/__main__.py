from argparse import ArgumentParser

from uvicorn import run

from . import __version__


def main(args=None):
    """Run the papermill_service, or query the version with --version."""
    parser = ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(args)
    run("papermill_service.app:app")


# test with: python -m papermill_service
if __name__ == "__main__":
    main()
