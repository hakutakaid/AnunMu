from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import LOG_GROUP_ID
from MusicIndo import app
from MusicIndo.utils.database import delete_served_chat, get_assistant


@app.on_message(filters.new_chat_members)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
                )
                msg = (
                    f"<blockquote><b>**ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ #New_Group**\n\n</b><blockquote>"
                    f"<blockquote><b>**ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n</b><blockquote>"
                    f"<blockquote><b>**ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n</b><blockquote>"
                    f"<blockquote><b>**ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ:** @{username}\n</b><blockquote>"
                    f"<blockquote><b>**ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ᴄᴏᴜɴᴛ:** {count}\n</b><blockquote>"
                    f"<blockquote><b>**ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}</b><blockquote>"
                )
                await app.send_message(
                    LOG_GROUP_ID,
                    text=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"ᴀᴅᴅᴇᴅ ʙʏ",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == app.id:
            remove_by = (
                message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            )
            chat_id = message.chat.id
            left = f"<blockquote><b>✫ <b><u>#Left_group</u></b> ✫\nᴄʜᴀᴛ ɴᴀᴍᴇ : {title}\nᴄʜᴀᴛ ɪᴅ : {chat_id}\n\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remove_by}</b><blockquote>"
            await app.send_message(LOG_GROUP_ID, text=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        print(f"Error: {e}")
