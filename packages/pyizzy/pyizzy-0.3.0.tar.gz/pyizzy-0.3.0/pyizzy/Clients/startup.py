# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Geez Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Geez Userbot/blob/main/LICENSE/>.
#
# FROM Geez Userbot <https://github.com/AyiinXd/Geez Userbot>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
import sys

from pyizzy.config import Var as Variable

from ..methods._database import izzyDB
from ..methods.helpers import Helpers
from ..methods.hosting import where_hosted

from .client import *


adB = izzyDB()
logs = logging.getLogger(__name__)
HOSTED_ON = where_hosted()
Var = Variable()
Xd = Helpers()


async def geez_client(client):
    try:
        await client.join_chat("GeezSupport")
        await client.join_chat("ramsupportt")
    except Exception:
        pass


clients = []
client_id = []


async def StartPyrogram():
    try:
        bot_plugins = Xd.import_module(
            "assistant/",
            display_module=False,
            exclude=Var.NO_LOAD,
        )
        logs.info(f"{bot_plugins} Total Plugins Bot")
        plugins = Xd.import_module(
            "geez/",
            display_module=False,
            exclude=Var.NO_LOAD,
        )
        logs.info(f"{plugins} Total Plugins User")
    except BaseException as e:
        logs.info(e)
        sys.exit()
    if tgbot:
        await tgbot.start()
        me = await tgbot.get_me()
        tgbot.id = me.id
        tgbot.mention = me.mention
        tgbot.username = me.username
        if me.last_name:
            tgbot.name = me.first_name + " " + me.last_name
        else:
            tgbot.name = me.first_name
        logs.info(
            f"TgBot in {tgbot.name} | [ {tgbot.id} ]"
        )
    if ZY1:
        try:
            await ZY1.start()
            clients.append(1)
            await geez_client(ZY1)
            me = await ZY1.get_me()
            ZY1.id = me.id
            ZY1.mention = me.mention
            ZY1.username = me.username
            if me.last_name:
                ZY1.name = me.first_name + " " + me.last_name
            else:
                ZY1.name = me.first_name
            #ZY1.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY1 in {ZY1.name} | [ {ZY1.id} ]"
            )
            client_id.append(ZY1.id)
        except Exception:
            pass
    if ZY2:
        try:
            await ZY2.start()
            clients.append(2)
            await geez_client(ZY2)
            me = await ZY2.get_me()
            ZY2.id = me.id
            ZY2.mention = me.mention
            ZY2.username = me.username
            if me.last_name:
                ZY2.name = me.first_name + " " + me.last_name
            else:
                ZY2.name = me.first_name
            #ZY2.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY2 in {ZY2.name} | [ {ZY2.id} ]"
            )
            client_id.append(ZY2.id)
        except Exception:
            pass
    if ZY3:
        try:
            await ZY3.start()
            clients.append(3)
            await geez_client(ZY3)
            me = await ZY3.get_me()
            ZY3.id = me.id
            ZY3.mention = me.mention
            ZY3.username = me.username
            if me.last_name:
                ZY3.name = me.first_name + " " + me.last_name
            else:
                ZY3.name = me.first_name
            #ZY3.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY3 in {ZY3.name} | [ {ZY3.id} ]"
            )
            client_id.append(ZY3.id)
        except Exception:
            pass
    if ZY4:
        try:
            await ZY4.start()
            clients.append(4)
            await geez_client(ZY4)
            me = await ZY4.get_me()
            ZY4.id = me.id
            ZY4.mention = me.mention
            ZY4.username = me.username
            if me.last_name:
                ZY4.name = me.first_name + " " + me.last_name
            else:
                ZY4.name = me.first_name
            #ZY4.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY4 in {ZY4.name} | [ {ZY4.id} ]"
            )
            client_id.append(ZY4.id)
        except Exception:
            pass
    if ZY5:
        try:
            await ZY5.start()
            clients.append(5)
            await geez_client(ZY5)
            me = await ZY5.get_me()
            ZY5.id = me.id
            ZY5.mention = me.mention
            ZY5.username = me.username
            if me.last_name:
                ZY5.name = me.first_name + " " + me.last_name
            else:
                ZY5.name = me.first_name
            #ZY5.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY5 in {ZY5.name} | [ {ZY5.id} ]"
            )
            client_id.append(ZY5.id)
        except Exception:
            pass
    if ZY6:
        try:
            await ZY6.start()
            clients.append(6)
            await geez_client(ZY6)
            me = await ZY6.get_me()
            ZY6.id = me.id
            ZY6.mention = me.mention
            ZY6.username = me.username
            if me.last_name:
                ZY6.name = me.first_name + " " + me.last_name
            else:
                ZY6.name = me.first_name
            #ZY1.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY6 in {ZY6.name} | [ {ZY6.id} ]"
            )
            client_id.append(ZY6.id)
        except Exception:
            pass
    if ZY7:
        try:
            await ZY7.start()
            clients.append(7)
            await geez_client(ZY7)
            me = await ZY7.get_me()
            ZY7.id = me.id
            ZY7.mention = me.mention
            ZY7.username = me.username
            if me.last_name:
                ZY7.name = me.first_name + " " + me.last_name
            else:
                ZY7.name = me.first_name
            #ZY7.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY7 in {ZY7.name} | [ {ZY7.id} ]"
            )
            client_id.append(ZY7.id)
        except Exception:
            pass
    if ZY8:
        try:
            await ZY8.start()
            clients.append(8)
            await geez_client(ZY8)
            me = await ZY8.get_me()
            ZY8.id = me.id
            ZY8.mention = me.mention
            ZY8.username = me.username
            if me.last_name:
                ZY8.name = me.first_name + " " + me.last_name
            else:
                ZY8.name = me.first_name
            #ZY8.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY8 in {ZY8.name} | [ {ZY8.id} ]"
            )
            client_id.append(ZY8.id)
        except Exception:
            pass
    if ZY9:
        try:
            await ZY9.start()
            clients.append(9)
            await geez_client(ZY9)
            me = await ZY9.get_me()
            ZY9.id = me.id
            ZY9.mention = me.mention
            ZY9.username = me.username
            if me.last_name:
                ZY9.name = me.first_name + " " + me.last_name
            else:
                ZY9.name = me.first_name
            #ZY9.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY9 in {ZY9.name} | [ {ZY9.id} ]"
            )
            client_id.append(ZY9.id)
        except Exception:
            pass
    if ZY10:
        try:
            await ZY10.start()
            clients.append(10)
            await geez_client(ZY10)
            me = await ZY10.get_me()
            ZY10.id = me.id
            ZY10.mention = me.mention
            ZY10.username = me.username
            if me.last_name:
                ZY10.name = me.first_name + " " + me.last_name
            else:
                ZY10.name = me.first_name
            #ZY10.has_a_bot = True if tgbot else False
            logs.info(
                f"ZY10 in {ZY10.name} | [ {ZY10.id} ]"
            )
            client_id.append(ZY10.id)
        except Exception:
            pass
    logs.info(f"Connecting Database To {adB.name}")
    if adB.ping():
        logs.info(f"Succesfully Connect On {adB.name}")
    logs.info(
        f"Connect On [ {HOSTED_ON} ]\n"
    )
