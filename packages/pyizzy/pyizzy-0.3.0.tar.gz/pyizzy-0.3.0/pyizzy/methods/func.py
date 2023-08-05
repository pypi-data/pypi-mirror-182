# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import asyncio
import multiprocessing
import os
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps


def update_envs():
    """Update Var. attributes to adB"""
    from .. import adB

    for envs in list(os.environ):
        if envs in ["LOG_CHAT", "BOT_TOKEN"] or envs in adB.keys():
            adB.set_key(envs, os.environ[envs])


def run_async(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        return await asyncio.get_event_loop().run_in_executor(
            ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 5),
            partial(function, *args, **kwargs),
        )

    return wrapper
