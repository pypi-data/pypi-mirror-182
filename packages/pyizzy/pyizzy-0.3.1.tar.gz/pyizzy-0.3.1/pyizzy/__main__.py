import asyncio
import importlib

from geezlibs import idle

from pyizzy import __version__

from . import *

from .config import Var
from .Clients.startup import StartPyrogram
from .exceptions import DependencyMissingError

yins = Var()
xd = PyrogramGeez()


try:
    from uvloop import install
except:
    install = None
    logs.info("'uvloop' not installed\ninstall 'uvloop' or add 'uvloop' in requirements.txt")


MSG_ON = """
<b>**GeezPyro v{BOT_VER} is back up and running!**ɴ</b>
"""

async def start_main():
    await StartPyrogram()
    try:
        await tgbot.send_message(
            yins.LOG_CHAT,
            MSG_ON.format(
                __version__,
                HOSTED_ON,
                geez_ver, 
                len(CMD_HELP),
            )
        )
    except BaseException as s:
        print(s)
    print(f"GeezUbot Version - {geez_ver}\n[🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    print(f"Starting GeezUbot - {geez_ver}")
    install()
    loop.run_until_complete(start_main())
