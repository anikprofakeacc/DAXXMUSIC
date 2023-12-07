from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging


##### Bing
@app.on_message(
    filters.command(
        ["bard", "askbard"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]
    )
)

async def bardapibot(bot, message):
    try:
        if message.reply_to_message:
            if message.reply_to_message.text:
                text = message.reply_to_message.text
            
                response = requests.get(url).json()
                text= response["text"]

            else:
                return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
        else:
            try:
                text = message.text.split(None, 1)[1]

            except IndexError:
                return await message.reply_text(
                    "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.\n Exᴀᴍᴘʟᴇ:\n\n/bard How r u?"
                )
        m = await message.reply_text(
                f"{message.from_user.first_name} Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ Qᴜᴇʀʏ....."
            )
        url = f"https://api.safone.dev/bard?message={text}"
        response = requests.get(url)
        out = response.json()
        output = out["choices"][0]["content"][0]
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        
        await m.reply(f"{output}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @catchme_here",
                                parse_mode=ParseMode.MARKDOWN,
                                
                            )
                

    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ: {e}")
