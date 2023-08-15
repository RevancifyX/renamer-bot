from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"""**👋 Hello, {user.mention} \n\nI am an Advance file Renamer and file Converter BOT with permanent and custom thumbnail support.\n\nSend me any video or document !**"""
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('📢 Updates', url='https://t.me/official_bins'),
        InlineKeyboardButton('🤝 Support', url='https://t.me/officialbins_chat')
        ],[
        InlineKeyboardButton('Commands', callback_data='help')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**File Name** - `{filename}`\n\n**File Size** - `{filesize}`"""
        buttons = [[ InlineKeyboardButton("Rename 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("Cancel ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**File Name** - `{filename}`\n\n**File Size** - `{filesize}`"""
        buttons = [[ InlineKeyboardButton("Rename 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("Cancel ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            txt=f"""**👋 Hello, {user.mention} \n\nI am an Advance file Renamer and file Converter BOT with permanent and custom thumbnail support.\n\nSend me any video or document !**"""
    reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton('📢 Updates', url='https://t.me/official_bins'),
        InlineKeyboardButton('🤝 Support', url='https://t.me/officialbins_chat')
        ],[
        InlineKeyboardButton('Commands', callback_data='help')
        ]
        ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Contact Admin ❣️", url="https://www.instagram.com/LazyDeveloperrr")
               ],[
               InlineKeyboardButton("❤️‍🔥 How to use me ? ❤️‍🔥", url='https://www.youtube.com/channel/UCY-iDra0x2hdd9PdHKcZkRw')
               ],[
               InlineKeyboardButton("🎬 Join our Movie Channel 🎬", url="https://t.me/+WwDm2ByFlz80YTY9")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Developer ❣️", url="https://www.instagram.com/LazyDeveloperrr")
               ],[
               InlineKeyboardButton("❤️‍🔥 How to make me ? ❤️‍🔥", url='https://www.youtube.com/channel/UCY-iDra0x2hdd9PdHKcZkRw')
               ],[
                InlineKeyboardButton("🎬 Join our Movie Channel 🎬", url="https://t.me/+WwDm2ByFlz80YTY9")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Developer ❣️", url="https://www.instagram.com/LazyDeveloperrr")
               ],[
               InlineKeyboardButton("❤️‍🔥 How to make me ? ❤️‍🔥", url='https://www.youtube.com/channel/UCY-iDra0x2hdd9PdHKcZkRw')
               ],[
                InlineKeyboardButton("🎬 Join our Movie Channel 🎬", url="https://t.me/+WwDm2ByFlz80YTY9")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





