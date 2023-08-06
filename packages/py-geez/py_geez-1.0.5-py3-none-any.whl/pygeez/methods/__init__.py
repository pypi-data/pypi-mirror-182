# py - geez
# Copyright (C) 2022-2023 @geezXd
#
# This file is a part of < https://github.com/geezXd/pygeez >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/geezXd/pygeez/blob/main/LICENSE/>.
#
# FROM py-geez <https://github.com/geezXd/pygeez>
# t.me/geezChat & t.me/geezSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from ._database import geezDB
from ._misc import _Misc
from .converter import Convert
from .func import update_envs
from .helpers import Helpers
from .hosting import where_hosted
from .Inline import InlineBot
from .queue import Queue


class Methods(
    _Misc,
    Convert,
    InlineBot,
    Helpers,
    Queue,
):
    pass
