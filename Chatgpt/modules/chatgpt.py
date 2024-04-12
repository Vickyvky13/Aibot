# -----------CREDITS -----------
# telegram : @python_coderx
# github : noob-mukesh
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import Mukesh
from config import *
from ..modules.buttons import *
from pyrogram.enums import ChatAction
from MukeshAPI import api
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chatgpt_chat(bot, message):
    
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt write simple website code using html css ,js?`")
    else:
        a = message.text.split(' ', 1)[1]

    # -----------CREDITS -----------
    # telegram : @python_coderx
    # github : noob-mukesh
    

    try:
        response = api.gemini(a)
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n||🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @solotreee|| ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)  
        
            
    except requests.exceptions.RequestException as e:
        pass
        
