
# FROM py-Ayiin <https://github.com/AyiinXd/pyIzzy>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from ._database import izzyDB
from ._misc import _Misc
from .converter import Convert
from .func import update_envs
from .helpers import Helpers
from .hosting import where_hosted
from .queue import Queue


class Methods(
    _Misc,
    Convert,
    Helpers,
    Queue,
):
    pass
