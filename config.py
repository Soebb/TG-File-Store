import os
from pyrogram import filters

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
DB_CHANNEL_ID = "-1001448973320"
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
sudousers = [292991814, 1601268629]
sudofilter = filters.user(sudousers)
