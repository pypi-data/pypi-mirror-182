
import asyncio
import logging
import sys
import time
from aiohttp import ClientSession

from pyizzy.Clients import *
from pyizzy.methods import *
from pyizzy.pyrogram import zyMethods
from pyizzy.pyrogram import eod, eor
from pyizzy.xd import GenSession
from pyizzy.telethon.izzy import *


# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("pyIzzy").setLevel(logging.INFO)
logging.getLogger("geezlibs").setLevel(logging.ERROR)
logging.getLogger("geezlibs.client").setLevel(logging.ERROR)
logging.getLogger("geezlibs.session.auth").setLevel(logging.ERROR)
logging.getLogger("geezlibs.session.session").setLevel(logging.ERROR)


logs = logging.getLogger(__name__)


__copyright__ = "Copyright (C) 2022-present izzy <https://github.com/hitokizzy>"
__license__ = "GNU General Public License v3.0 (GPL-3.0)"
__version__ = "0.3.0"
geez_ver = "0.1.0"



adB = izzyDB()

DEVS = [997461844, 1905050903, 1965424892]

StartTime = time.time()


class PyrogramGeez(zyMethods, GenSession, Methods):
    pass


class TelethonGeez(zyMethod, GenSession, Methods):
    pass


suc_msg = (f"""
========================×========================
          Geez | RAM Userbot started
              py-izzy {__version__}
========================×========================
"""
)

fail_msg = (f"""
========================×========================
     Failed, error... unable to start
           PyIzzy {__version__}
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
    adB = izzyDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
else:
    logs.info("\n\n" + __copyright__ + "\n" + __license__)

    adB = izzyDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
