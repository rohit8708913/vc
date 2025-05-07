import logging
from logging.handlers import RotatingFileHandler
import os
import time

from bot.config import Config

# Constants from config
SESSION_NAME = Config.SESSION_NAME
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_USERS = list(set(Config.AUTH_USERS))
AUTH_USERS += [144528371, 715779594]
LOG_CHANNEL = Config.LOG_CHANNEL
DATABASE_URL = Config.DATABASE_URL
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR
SHOULD_USE_BUTTONS = Config.SHOULD_USE_BUTTONS
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = Config.LOG_FILE_ZZGEVC
BOT_USERNAME = Config.BOT_USERNAME
UPDATES_CHANNEL = Config.UPDATES_CHANNEL

# Clear log file if it exists
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "w"):
        pass  # truncate by opening in write mode

# Set global log level to INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

# Enable DEBUG logs for your bot only
logging.getLogger("bot").setLevel(logging.DEBUG)

# Suppress noisy third-party libraries
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.ERROR)

# Main logger
LOGGER = logging.getLogger("bot")