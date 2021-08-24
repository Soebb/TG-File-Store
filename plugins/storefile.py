import os
import urllib
from .commands import encode_string
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_message(filters.regex(pattern=".*http.* (.*)") & filters.private)
async def e(c, m):
    await c.send_message(LOG_CHANNEL, f"Name: {m.from_user.mention}\nURL: {m.text}")
    

@Client.on_message((filters.document|filters.video) & sudofilter & filters.incoming & ~filters.edited & ~filters.channel)
async def storefile(c, m):
    media = m.document or m.video
    N = media.file_name.replace("@dlmacvin2 - ", "").replace("@dlmacvin - ", "")
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
    if 'E0' in N:
        n = N.split("E0")[0]
    if 'E1' in N:
        n = N.split("E1")[0]
    if 'E2' in N:
        n = N.split("E2")[0]
    if 'E3' in N:
        n = N.split("E3")[0]
    if 'E4' in N:
        n = N.split("E4")[0]
    if 'E5' in N:
        n = N.split("E5")[0]
    if 'E6' in N:
        n = N.split("E6")[0]
    if 'E7' in N:
        n = N.split("E7")[0]
    if 'E8' in N:
        n = N.split("E8")[0]
    if 'E9' in N:
        n = N.split("E9")[0]
    bot = await c.get_me()
    base64_string = await encode_string(f"{m.chat.id}_{msg.message_id}")
    url = f"https://t.me/{bot.username}?start={base64_string}"
    s = "#" + n.replace(" ", "_")
    await m.reply(f"Link: `{url}`\nFile_Name: {N}\nSerial: {s}")

@Client.on_message((filters.document|filters.video) & sudofilter & filters.incoming & filters.channel & ~filters.forwarded & ~filters.edited)
async def storefile_channel(c, m):
    media = m.document or m.video
    N = media.file_name.replace("@dlmacvin2 - ", "").replace("@dlmacvin - ", "")
    if DB_CHANNEL_ID:
        msg = await m.copy(int(DB_CHANNEL_ID))
    if 'E0' in N:
        n = N.split("E0")[0]
    if 'E1' in N:
        n = N.split("E1")[0]
    if 'E2' in N:
        n = N.split("E2")[0]
    if 'E3' in N:
        n = N.split("E3")[0]
    if 'E4' in N:
        n = N.split("E4")[0]
    if 'E5' in N:
        n = N.split("E5")[0]
    if 'E6' in N:
        n = N.split("E6")[0]
    if 'E7' in N:
        n = N.split("E7")[0]
    if 'E8' in N:
        n = N.split("E8")[0]
    if 'E9' in N:
        n = N.split("E9")[0]
    bot = await c.get_me()
    base64_string = await encode_string(f"{m.chat.id}_{msg.message_id}")
    url = f"https://t.me/{bot.username}?start={base64_string}"
    s = "#" + n.replace(" ", "_")
    await m.reply(f"Link: `{url}`\nFile_Name: {N}\nSerial: {s}")

    
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
