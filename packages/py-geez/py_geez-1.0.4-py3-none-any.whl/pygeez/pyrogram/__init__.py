# py - geez
# Copyright (C) 2022-2023 @geezXd
#
# This file is a part of < https://github.com/geezXd/pygeez >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/geezXd/pygeez/blob/main/LICENSE/>.
#
# FROM py-geez <https://github.com/geezXd/pygeez>
# t.me/geezChat & t.me/geezSupport

from ._wrappers import eod, eor
from .func import Function
from .misc import Misc
from .pastebin import PasteBin, paste, post, s_paste
from .sections import section
from .toolbot import ToolBot
from .tools import Tools


class geezMethods(
    Function,
    Misc,
    ToolBot,
    Tools,
):
    pass
