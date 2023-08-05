
from time import time
from datetime import datetime

from geezlibs import __version__ as pyrver, Client
from geezlibs.enums import ParseMode
from pyrogram.raw.functions import Ping
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
from platform import python_version

from ..config import Var as Variable
from ..Clients import *

from ._database import izzyDB
from .hosting import where_hosted

adB = izzyDB()
var = Variable()
HOSTED_ON = where_hosted()


class _Misc(object):
    async def alive(self, cb: str):
        from pyizzy import __version__
        from pyizzy import CMD_HELP
        
        output = (
            f"**[Geez Userbot](https://github.com/hitokizzy)**\n\n"
            f"**{var.ALIVE_TEXT}**\n\n"
        )
        buttons = [
            [
                InlineKeyboardButton("Help Menu", callback_data=cb),
            ]
        ]
        results=[
            (
                InlineQueryResultPhoto(
                    photo_url=Var.ALIVE_PIC,
                    title="Alive",
                    description="inline GeezUbot.",
                    caption=output,
                    reply_markup=InlineKeyboardMarkup(
                        buttons
                    ),
                    parse_mode=ParseMode.MARKDOWN,
                )
            )
        ]
        return results
    
    async def info_inline_func(self, client: Client, answers, peer):
        not_found = InlineQueryResultArticle(
            title="PEER NOT FOUND",
            input_message_content=InputTextMessageContent("PEER NOT FOUND"),
        )
        try:
            user = await client.get_users(peer)
            caption, _ = await self.get_user_info(user, True)
        except IndexError:
            try:
                chat = await client.get_chat(peer)
                caption, _ = await self.get_chat_info(chat, True)
            except Exception:
                return [not_found]
        except Exception:
            return [not_found]

        answers.append(
            InlineQueryResultArticle(
                title="Found Peer.",
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
            )
        )
    
    
