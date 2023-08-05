import asyncio
import logging
import sys
import time
from aiohttp import ClientSession

from pyGeez.Clients import *
from pyGeez.methods import *
from pyGeez.pyrogram import GeezMethods
from pyGeez.pyrogram import eod, eor
from pyGeez.gp import GenSession
from pyGeez.telethon.geez import *


# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("pyGeez").setLevel(logging.INFO)
logging.getLogger("fipper").setLevel(logging.ERROR)
logging.getLogger("fipper.client").setLevel(logging.ERROR)
logging.getLogger("fipper.session.auth").setLevel(logging.ERROR)
logging.getLogger("fipper.session.session").setLevel(logging.ERROR)


logs = logging.getLogger(__name__)


__copyright__ = "Copyright (C) 2022-present vckyou <https://github.com/vckyou>"
__license__ = "GNU General Public License v3.0 (GPL-3.0)"
__version__ = "1.0.3"
geez_ver = "0.1"


adB = GeezDB()

DEVS = [874946835]

StartTime = time.time()


class Pyrograms(GeezMethods, GenSession, Methods):
    pass


class Telethons(GeezMethod, GenSession, Methods):
    pass


suc_msg = (f"""
========================×========================
          GeezProject Userbot started
              py-Geez {__version__}
========================×========================
"""
)

fail_msg = (f"""
========================×========================
    There was an error in committing. 
        Please contact @GeezSupport {__version__}
========================×========================
"""
)


run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True

    from .decorator import *

    print("\n\n" + __copyright__ + "\n" + __license__)
    print(suc_msg)

    update_envs()

    CMD_HELP = {}
    adB = GeezDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
else:
    logs.info("\n\n" + __copyright__ + "\n" + __license__)

    adB = GeezDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
