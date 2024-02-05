from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://arthur:arthur0@cluster0.g5ihsk1.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "a4476bdb326701fdadfe834593db59eb"]
        API_ID = [int, 2663335]
        BOT_TOKEN = [str, "6978317893:AAH4nprdiR7YSVD6n__wWXYRLAYyeRJXoLc"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 100]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[1922494807]]
        OWNER_ID = [int, 953362604]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/HuntersOrgUpdates"]
        FORCEJOIN_ID = [int,-1001804191007]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
