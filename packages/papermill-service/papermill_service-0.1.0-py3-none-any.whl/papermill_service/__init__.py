from importlib.metadata import version

__version__ = version("papermill_service")
del version

__all__ = ["__version__"]
