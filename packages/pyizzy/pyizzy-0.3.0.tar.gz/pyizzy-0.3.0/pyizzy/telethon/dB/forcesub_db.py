# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.


from .. import adB


def get_chats():
    return adB.get_key("FORCESUB") or {}


def add_forcesub(chat_id, chattojoin):
    omk = get_chats()
    omk.update({chat_id: chattojoin})
    return adB.set_key("FORCESUB", omk)


def get_forcesetting(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        return omk[chat_id]


def rem_forcesub(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        try:
            del omk[chat_id]
            return adB.set_key("FORCESUB", omk)
        except KeyError:
            return False
