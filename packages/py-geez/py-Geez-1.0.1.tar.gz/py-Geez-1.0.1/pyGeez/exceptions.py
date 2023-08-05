# py - Geez
# Copyright (C) 2022-2023 @vckyou
#
# This file is a part of < https://github.com/vckyou/pyGeez >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/vckyou/pyGeez/blob/main/LICENSE/>.
#
# FROM py-Geez <https://github.com/vckyou/pyGeez>
# t.me/GeezChat & t.me/GeezSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

"""
Exceptions which can be raised by py-Geez Itself.
"""


class pyGeezError(Exception):
    ...


class PyrogramMissingError(ImportError):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyGeezError):
    ...


class SpamFailed(Exception):
    ...


class DownloadFailed(Exception):
    ...


class DelAllFailed(Exception):
    ...


class FFmpegReturnCodeError(Exception):
    ...
