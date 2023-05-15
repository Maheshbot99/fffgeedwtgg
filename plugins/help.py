"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('help'))
async def upgrade(bot,update):
	text = """ **📚 ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ :**
➢ /start - **ᴄʜᴇᴄᴋ ɪ'ᴍ ᴀʟɪᴠᴇ**
➢ /myplan - **ᴄʜᴇᴄᴋ yᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ**
➢ /upgrade - **ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴩʟᴀɴ ɪɴꜰᴏ**
➢ /settings - **ᴄᴏɴꜰɪɢᴜʀᴇ yᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ**
➢ /set_caption - **ᴛᴏ ᴀᴅᴅ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /see_caption - **ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /del_caption - **ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /viewthumb - **ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ !!**
➢ /delthumb - **ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ !!**

**• ᴜᴩɢʀᴀᴅᴇ yᴏᴜʀ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇɴᴀᴍɪɴɢ ᴇxᴩᴇʀɪᴇɴᴄᴇ.**
**• ꜱᴇɴᴅ ᴀ ᴩʜᴏᴛᴏ ᴛᴏ ᴍᴇ ᴛᴏ ᴀᴅᴅ ᴀꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ**
**• ꜱᴇɴᴅ yᴏᴜʀ ꜰɪʟᴇꜱ ᴛᴏ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("⚙  ꜱᴇᴛᴛɪɴɢꜱ ",callback_data = "settings")], 
        			[InlineKeyboardButton("🫨 ʀᴇꜱᴛᴀʀᴛ ʙᴏᴛ",callback_data = "restart"),
        			InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ",callback_data = "upgrade")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["help"]))
async def upgradecm(bot,message):
	text = """ **📚 ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ :**
➢ /start - **ᴄʜᴇᴄᴋ ɪ'ᴍ ᴀʟɪᴠᴇ**
➢ /myplan - **ᴄʜᴇᴄᴋ yᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ**
➢ /upgrade - **ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴩʟᴀɴ ɪɴꜰᴏ**
➢ /settings - **ᴄᴏɴꜰɪɢᴜʀᴇ yᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ**
➢ /set_caption - **ᴛᴏ ᴀᴅᴅ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /see_caption - **ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /del_caption - **ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**
➢ /viewthumb - **ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ !!**
➢ /delthumb - **ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ !!**

**• ᴜᴩɢʀᴀᴅᴇ yᴏᴜʀ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇɴᴀᴍɪɴɢ ᴇxᴩᴇʀɪᴇɴᴄᴇ.**
**• ꜱᴇɴᴅ ᴀ ᴩʜᴏᴛᴏ ᴛᴏ ᴍᴇ ᴛᴏ ᴀᴅᴅ ᴀꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ**
**• ꜱᴇɴᴅ yᴏᴜʀ ꜰɪʟᴇꜱ ᴛᴏ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "settings")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "restart"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "upgrade")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
