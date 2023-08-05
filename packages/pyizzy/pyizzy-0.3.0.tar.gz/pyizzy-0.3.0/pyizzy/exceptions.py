# py - Ayiin
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/pyIzzy >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/py-izzyblob/main/LICENSE/>.
#
# FROM py-Ayiin <https://github.com/AyiinXd/pyIzzy>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

"""
Exceptions which can be raised by py-Ayiin Itself.
"""


class pyIzzyError(Exception):
    ...


class PyrogramMissingError(ImportError):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyIzzyError):
    ...


class SpamFailed(Exception):
    ...


class DownloadFailed(Exception):
    ...


class DelAllFailed(Exception):
    ...


class FFmpegReturnCodeError(Exception):
    ...
