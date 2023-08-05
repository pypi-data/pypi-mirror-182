from geezlibs import Client

from ..config import Var as Variable

Var = Variable()

hndlr = f"{Var.HNDLR[0]} {Var.HNDLR[1]} {Var.HNDLR[2]} {Var.HNDLR[3]} {Var.HNDLR[4]} {Var.HNDLR[5]}"


tgbot = (
    Client(
        name="tgbot",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        bot_token=Var.BOT_TOKEN,
    )
)

# For Publik Repository
ZY1 = (
    Client(
        name="ZY1",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_1,
        in_memory=True,
    )
    if Var.STRING_1
    else None
)


ZY2 = (
    Client(
        name="ZY2",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_2,
        in_memory=True,
    )
    if Var.STRING_2
    else None
)
        
ZY3 = (
    Client(
        name="ZY3",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_3,
        in_memory=True,
    )
    if Var.STRING_3
    else None
)

ZY4 = (
    Client(
        name="ZY4",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_4,
        in_memory=True,
    )
    if Var.STRING_4
    else None
)

ZY5 = (
    Client(
        name="ZY5",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_5,
        in_memory=True,
    )
    if Var.STRING_5
    else None
)

ZY6 = (
    Client(
        name="ZY6",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_6,
        in_memory=True,
    )
    if Var.STRING_6
    else None
)


ZY7 = (
    Client(
        name="ZY7",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_7,
        in_memory=True,
    )
    if Var.STRING_7
    else None
)
        
ZY8 = (
    Client(
        name="ZY8",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_8,
        in_memory=True,
    )
    if Var.STRING_8
    else None
)


ZY9 = (
    Client(
        name="ZY9",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_9,
        in_memory=True,
    )
    if Var.STRING_9
    else None
)
ZY10 = (
    Client(
        name="ZY10",
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        session_string=Var.STRING_10,
        in_memory=True,
    )
    if Var.STRING_10
    else None
)


Bots = [
    bot for bot in [
        ZY1, 
        ZY2, 
        ZY3, 
        ZY4, 
        ZY5, 
        ZY6, 
        ZY7, 
        ZY8,
        ZY9,
        ZY10,
    ] if bot
]
