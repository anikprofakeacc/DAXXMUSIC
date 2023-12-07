import os, time
import openai
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS



openai.api_key = "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"




@app.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app :app, message):
    
    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.ask How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        






@app.on_message(filters.command(["assis"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(app :app, message):
    
    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.assis How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            text = x    
            tts = gTTS(text, lang='en')
            tts.save('output.mp3')
            await app.send_voice(chat_id=message.chat.id, voice='output.mp3')
            os.remove('output.mp3')            
            
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ") 



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
