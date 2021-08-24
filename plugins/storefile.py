import os
import urllib
from .commands import encode_string
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_message(filters.regex(pattern=".*http.* (.*)") & 
async def e(c, m):
    await c.send_message(LOG_CHANNEL, f"Name: {m.from_user.mention}\nURL: {m.text}")
    


@Client.on_message((filters.document|filters.video) & filters.incoming & ~filters.edited & ~filters.channel)
async def storefile(c, m):
    media = m.document or m.video
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
        
    bot = await c.get_me()
    base64_string = await encode_string(f"{m.chat.id}_{msg.message_id}")
    url = f"https://t.me/{bot.username}?start={base64_string}"

    await m.reply(f"link = `{url}`\n#

@Client.on_message((filters.document|filters.video) & filters.incoming & filters.channel & ~filters.forwarded & ~filters.edited)
async def storefile_channel(c, m):
    media = m.document or m.video

    text = ""
    # if databacase channel exist forwarding message to channel
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))

    # creating urls
    bot = await c.get_me()
    base64_string = await encode_string(f"{m.chat.id}_{msg.message_id}")
    url = f"https://t.me/{bot.username}?start={base64_string}"
   
    await m.reply(f"link = `{url}`\n#

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " days, ") if days else "") + \
        ((str(hours) + " hrs, ") if hours else "") + \
        ((str(minutes) + " min, ") if minutes else "") + \
        ((str(seconds) + " sec, ") if seconds else "") + \
        ((str(milliseconds) + " millisec, ") if milliseconds else "")
    return tmp[:-2]
