"""
Exceptions which can be raised by py-Ayiin Itself.
"""


class pygeezError(Exception):
    ...


class PyrogramMissingError(ImportError):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pygeezError):
    ...


class SpamFailed(Exception):
    ...


class DownloadFailed(Exception):
    ...


class DelAllFailed(Exception):
    ...


class FFmpegReturnCodeError(Exception):
    ...
