import logging
from datetime import datetime
from traceback import format_exc
import pytz
from geezlibs import ContinuePropagation, StopPropagation, filters
from geezlibs.enums import ChatMemberStatus, ChatType
from geezlibs.errors.exceptions.bad_request_400 import (
    MessageIdInvalid,
    MessageNotModified,
    MessageEmpty,
    UserNotParticipant
)
from geezlibs.handlers import MessageHandler

from pyizzy.pyrogram import eor

from . import DEVS
from .config import Var as Variable
from .Clients import *


Var = Variable()


async def is_admin_or_owner(message, user_id) -> bool:
    """Check If A User Is Creator Or Admin Of The Current Group"""
    if message.chat.type in [ChatType.PRIVATE, ChatType.BOT]:
        # You Are Boss Of Pvt Chats.
        return True
    user_s = await message.chat.get_member(int(user_id))
    if user_s.status in (
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR):
        return True
    return False


def Zy(
    cmd: list,
    group: int = 0,
    devs: bool = False,
    pm_only: bool = False,
    group_only: bool = False,
    channel_only: bool = False,
    admin_only: bool = False,
    pass_error: bool = False,
    propagate_to_next_handler: bool = True,
):
    """- Main Decorator To Register Commands. -"""
    if not devs:
        filterm = (
            filters.me
            & filters.command(cmd, Var.HNDLR)
            & ~filters.via_bot
            & ~filters.forwarded
        )
    else:
        filterm = (
            filters.user(DEVS)
            & filters.command(cmd, "")
        )

    def decorator(func):
        async def wrapper(client, message):
            message.client = client
            chat_type = message.chat.type
            if admin_only and not await is_admin_or_owner(
                message, (client.me).id
            ):
                await eor(
                    message, "<code>This Command Only Works, If You Are Admin Of The Chat!</code>"
                )
                return
            if group_only and chat_type != (
                    ChatType.GROUP or ChatType.SUPERGROUP):
                await eor(message, "<code>Are you sure this is a group?</code>")
                return
            if channel_only and chat_type != ChatType.CHANNEL:
                await eor(message, "This Command Only Works In Channel!")
                return
            if pm_only and chat_type != ChatType.PRIVATE:
                await eor(message, "<code>This Cmd Only Works On PM!</code>")
                return
            if pass_error:
                await func(client, message)
            else:
                try:
                    await func(client, message)
                except StopPropagation:
                    raise StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModified:
                    pass
                except MessageIdInvalid:
                    logging.warning(
                        "Please Don't Delete Commands While it's Processing..."
                    )
                except UserNotParticipant:
                    pass
                except ContinuePropagation:
                    raise ContinuePropagation
                except BaseException:
                    logging.error(
                        f"Exception - {func.__module__} - {func.__name__}"
                    )
                    TZZ = pytz.timezone(Var.TZ)
                    datetime_tz = datetime.now(TZZ)
                    text = "<b>!ERROR - REPORT!</b>\n\n"
                    text += f"\n<b>Dari:</b> <code>{client.me.first_name}</code>"
                    text += f"\n<b>Trace Back : </b> <code>{str(format_exc())}</code>"
                    text += f"\n<b>Plugin-Name :</b> <code>{func.__module__}</code>"
                    text += f"\n<b>Function Name :</b> <code>{func.__name__}</code> \n"
                    text += datetime_tz.strftime(
                        "<b>Date :</b> <code>%Y-%m-%d</code> \n<b>Time :</b> <code>%H:%M:%S</code>"
                    )
                    try:
                        xx = await tgbot.send_message(Var.LOG_CHAT, text)
                        await xx.pin(disable_notification=False)
                    except BaseException:
                        logging.error(text)
        add_handler(filterm, wrapper, cmd)
        return wrapper

    return decorator


def listen(filter_s):
    """Simple Decorator To Handel Custom Filters"""
    def decorator(func):
        async def wrapper(client, message):
            try:
                await func(client, message)
            except StopPropagation:
                raise StopPropagation
            except ContinuePropagation:
                raise ContinuePropagation
            except UserNotParticipant:
                pass
            except MessageEmpty:
                pass
            except BaseException:
                logging.error(
                    f"Exception - {func.__module__} - {func.__name__}")
                TZZ = pytz.timezone(Var.TZ)
                datetime_tz = datetime.now(TZZ)
                text = "<b>!ERROR WHILE HANDLING UPDATES!</b>\n\n"
                text += f"\n<b>Dari:</b> <code>{client.me.first_name}</code>"
                text += f"\n<b>Trace Back : </b> <code>{str(format_exc())}</code>"
                text += f"\n<b>Plugin Name :</b> <code>{func.__module__}</code>"
                text += f"\n<b>Function Name :</b> <code>{func.__name__}</code> \n"
                text += datetime_tz.strftime(
                    "<b>Date :</b> <code>%Y-%m-%d</code> \n<b>Time :</b> <code>%H:%M:%S</code>"
                )
                try:
                    xx = await tgbot.send_message(Var.LOG_CHAT, text)
                    await xx.pin(disable_notification=False)
                except BaseException:
                    logging.error(text)
            message.continue_propagation()
        if ZY1:
            ZY1.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY2:
            ZY2.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY3:
            ZY3.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY4:
            ZY4.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY5:
            ZY5.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY6:
            ZY6.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY7:
            ZY7.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY8:
            ZY8.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY9:
            ZY9.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY10:
            ZY10.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        '''
        if ZY11:
            ZY11.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY12:
            ZY12.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY13:
            ZY13.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY14:
            ZY14.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY15:
            ZY15.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY16:
            ZY16.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY17:
            ZY17.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY18:
            ZY18.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY19:
            ZY19.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY20:
            ZY20.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY21:
            ZY21.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY22:
            ZY22.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY23:
            ZY23.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY24:
            ZY24.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY25:
            ZY25.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY26:
            ZY26.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY27:
            ZY27.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY28:
            ZY28.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY29:
            ZY29.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY30:
            ZY30.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY31:
            ZY31.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY32:
            ZY32.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY33:
            ZY33.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY34:
            ZY34.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY35:
            ZY35.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY36:
            ZY36.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY37:
            ZY37.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY38:
            ZY38.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY39:
            ZY39.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY40:
            ZY40.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY41:
            ZY41.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY42:
            ZY42.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY43:
            ZY43.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY44:
            ZY44.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY45:
            ZY45.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY46:
            ZY46.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY47:
            ZY47.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY48:
            ZY48.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY49:
            ZY49.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY50:
            ZY50.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY51:
            ZY51.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY52:
            ZY52.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY53:
            ZY53.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY54:
            ZY54.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY55:
            ZY55.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY56:
            ZY56.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY57:
            ZY57.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY58:
            ZY58.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY59:
            ZY59.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY60:
            ZY60.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY61:
            ZY61.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY62:
            ZY62.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY63:
            ZY63.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY64:
            ZY64.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY65:
            ZY65.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY66:
            ZY66.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY67:
            ZY67.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY68:
            ZY68.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY69:
            ZY69.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY70:
            ZY70.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY71:
            ZY71.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY72:
            ZY72.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY73:
            ZY73.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY74:
            ZY74.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY75:
            ZY75.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY76:
            ZY76.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY77:
            ZY77.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY78:
            ZY78.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY79:
            ZY79.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY80:
            ZY80.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY81:
            ZY81.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY82:
            ZY82.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY83:
            ZY83.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY84:
            ZY84.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY85:
            ZY85.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY86:
            ZY86.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY87:
            ZY87.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY88:
            ZY88.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY89:
            ZY89.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY90:
            ZY90.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY91:
            ZY91.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY92:
            ZY92.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY93:
            ZY93.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY94:
            ZY94.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY95:
            ZY95.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY96:
            ZY96.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY97:
            ZY97.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY98:
            ZY98.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY99:
            ZY99.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        if ZY100:
            ZY100.add_handler(
                MessageHandler(
                    wrapper,
                    filters=filter_s),
                group=0)
        '''
        return wrapper

    return decorator


def add_handler(filter_s, func_, cmd):
    if ZY1:
        ZY1.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY2:
        ZY2.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY3:
        ZY3.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY4:
        ZY4.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY5:
        ZY5.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY6:
        ZY6.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY7:
        ZY7.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY8:
        ZY8.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY9:
        ZY9.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY10:
        ZY10.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    '''
    if ZY11:
        ZY11.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY12:
        ZY12.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY13:
        ZY13.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY14:
        ZY14.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY15:
        ZY15.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY16:
        ZY16.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY17:
        ZY17.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY18:
        ZY18.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY19:
        ZY19.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY20:
        ZY20.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY21:
        ZY21.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY22:
        ZY22.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY23:
        ZY23.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY24:
        ZY24.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY25:
        ZY25.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY26:
        ZY26.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY27:
        ZY27.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY28:
        ZY28.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY29:
        ZY29.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY30:
        ZY30.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY31:
        ZY31.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY32:
        ZY32.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY33:
        ZY33.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY34:
        ZY34.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY35:
        ZY35.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY36:
        ZY36.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY37:
        ZY37.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY38:
        ZY38.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY39:
        ZY39.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY40:
        ZY40.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY41:
        ZY41.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY42:
        ZY42.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY43:
        ZY43.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY44:
        ZY44.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY45:
        ZY45.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY46:
        ZY46.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY47:
        ZY47.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY48:
        ZY48.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY49:
        ZY49.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY50:
        ZY50.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY51:
        ZY51.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY52:
        ZY52.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY53:
        ZY53.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY54:
        ZY54.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY55:
        ZY55.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY56:
        ZY56.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY57:
        ZY57.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY58:
        ZY58.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY59:
        ZY59.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY60:
        ZY60.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY61:
        ZY61.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY62:
        ZY62.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY63:
        ZY63.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY64:
        ZY64.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY65:
        ZY65.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY66:
        ZY66.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY67:
        ZY67.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY68:
        ZY68.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY69:
        ZY69.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY70:
        ZY70.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY71:
        ZY71.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY72:
        ZY72.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY73:
        ZY73.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY74:
        ZY74.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY75:
        ZY75.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY76:
        ZY76.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY77:
        ZY77.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY78:
        ZY78.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY79:
        ZY79.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY80:
        ZY80.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY81:
        ZY81.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY82:
        ZY82.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY83:
        ZY83.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY84:
        ZY84.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY85:
        ZY85.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY86:
        ZY86.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY87:
        ZY87.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY88:
        ZY88.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY89:
        ZY89.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY90:
        ZY90.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY91:
        ZY91.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY92:
        ZY92.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY93:
        ZY93.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY94:
        ZY94.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY95:
        ZY95.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY96:
        ZY96.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY97:
        ZY97.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY98:
        ZY98.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY99:
        ZY99.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    if ZY100:
        ZY100.add_handler(MessageHandler(func_, filters=filter_s), group=0)
    '''
