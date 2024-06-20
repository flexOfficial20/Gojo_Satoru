from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM")
    API_ID = int(config("API_ID", default="20533795"))
    API_HASH = config("API_HASH", default="f6cadf28523943f525e706e6ace8a250")
    OWNER_ID = int(config("OWNER_ID", default=6584789596))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", ""-1002100475470))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="6584789596",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="5702598840",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split(None)
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="mongodb+srv://Mongo1:586637515hshhwfftqu@cluster0.tvy79ai.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="cluster0")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="flex_support_chat")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="flex_bots_news")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "Ayanokoji_Kiyotaka_Robot"
    BOT_ID = "7116566735"
    BOT_NAME = "ᴀʏᴀɴᴏᴋᴏᴊɪ ᴋɪʏᴏᴛᴀᴋᴀ"
    owner_username = "FLEXdub_Official"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM"
    API_ID = 20533795  # Your APP_ID from Telegram
    API_HASH = "f6cadf28523943f525e706e6ace8a250"  # Your APP_HASH from Telegram
    OWNER_ID = 6584789596  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1002100475470  # Your Private Group ID for logs
    DEV_USERS = [6584789596]
    SUDO_USERS = [5702598840]
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://Mongo1:586637515hshhwfftqu@cluster0.tvy79ai.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "cluster0"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "flex_support_chat"
    SUPPORT_CHANNEL = "flex_bots_news"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
