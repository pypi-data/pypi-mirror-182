import asyncio
import logging
import sys
import time
from aiohttp import ClientSession

from pygeez.Clients import *
from pygeez.methods import *
from pygeez.pyrogram import geezMethods
from pygeez.pyrogram import eod, eor
from pygeez.xd import GenSession
from pygeez.telethon.geez import *


# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("pygeez").setLevel(logging.INFO)
logging.getLogger("pyroge").setLevel(logging.ERROR)
logging.getLogger("pyroge.client").setLevel(logging.ERROR)
logging.getLogger("pyroge.session.auth").setLevel(logging.ERROR)
logging.getLogger("pyroge.session.session").setLevel(logging.ERROR)


logs = logging.getLogger(__name__)


__copyright__ = "Copyright (C) 2022-present vckyou <https://github.com/vckyou>"
__license__ = "GNU General Public License v3.0 (GPL-3.0)"
__version__ = "1.0.5"
geez_ver = "0.0.1"


adB = geezDB()

DEVS = [997461844, 1905050903, 1965424892]

StartTime = time.time()


class PyrogramXd(geezMethods, GenSession, Methods):
    pass


class TelethonXd(geezMethod, GenSession, Methods):
    pass


suc_msg = (f"""
========================×========================
           Credit Py-geez {__version__}
========================×========================
"""
)

fail_msg = (f"""
========================×========================
      Commit Yang Bener Bego Biar Gak Error
           Credit Py-geez {__version__}
========================×========================
"""
)

start_bot = (f"""
========================×========================
         Starting geezUbot Version {geez_ver}
        Copyright (C) 2022-present vckyou
========================×========================
"""
)

run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True

    from .decorator import *

    print("\n\n" + __copyright__ + "\n" + __license__)
    print(start_bot)

    update_envs()

    CMD_HELP = {}
    adB = geezDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
else:
    print(suc_msg)
    print("\n\n" + __copyright__ + "\n" + __license__)
    print(fail_msg)

    adB = geezDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
