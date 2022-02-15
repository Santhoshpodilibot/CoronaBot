import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Corona-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.sumanjay.cf/covid/?country="

START_TEXT = """ʜᴇʟʟᴏ {},

ʜɪ ɴᴇɴᴜ ᴄᴏʀᴏɴᴀ ᴜᴘᴅᴀᴛᴇs ʙᴏᴛ ɴɪ ɴɪ ᴄᴏʀᴏɴᴀ ɢᴜʀɪɴᴄʜɪ ᴜᴘᴅᴀᴛᴇs ᴇsᴛʜᴀ. ᴊᴜsᴛ ᴇᴍɪ ʟᴇᴅʜᴜ ᴍᴇ ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ ᴇɴᴛᴇʀ ᴄʜᴇʏᴀɴᴅɪ ᴄʜᴀʟᴜ..💝

ᴍᴀᴅᴇ ʙʏ:@santhu_music_bot"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('😊 ᴏᴡɴᴇʀ 😊', url='https://t.me/santhu_music_bot')]])


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def reply_info(bot, update):
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(update.text),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--

ᴄᴏᴜɴᴛʀʏ : `{country}`
ᴀᴄᴛɪᴠᴇᴅ : `{active}`
ᴄᴏɴғɪʀᴍᴇᴅ : `{confirmed}`
ᴅᴇᴀᴛʜs : `{deaths}`
ɪᴅ : `{info_id}`
ʟᴀsᴛ ᴜᴘᴅᴀᴛᴇ : `{last_update}`
ʟᴀᴛɪᴛᴜᴅᴇ : `{latitude}`
ʟᴏɴɢɪᴛᴜᴅᴇ : `{longitude}`
ʀᴇᴄᴏᴠᴇʀᴇᴅ : `{recovered}`

ᴍᴀᴅᴇ ʙʏ:@santhu_music_bot"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('◁', callback_data='home')]])      
        return covid_info
    except Exception as error:
        return error



Bot.run()
