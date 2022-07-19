import random

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Hero import SUDOERS, app, random_assistant
from Hero.Database import get_assistant, save_assistant
from Hero.Utilities.assistant import get_assistant_details

__MODULE__ = "ᴀssɪsᴛᴀɴᴛ"
__HELP__ = f"""


`/checkassistant`
- ᴄʜᴇᴄᴋ ᴛʜᴇ ᴀʟʟᴏᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴏғ ʏᴏᴜʀ ᴄʜᴀᴛ


**ɴᴏᴛᴇ:**
-ᴏɴʟʏy ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs

`/changeassistant` [ᴀss ɴᴜᴍʙᴇʀ]
- ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘʀᴇᴠɪᴏɪᴜs ᴀʟʟᴏᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ɴᴇᴡ ᴏɴᴇ.

`/setassistant` [ᴀss ɴᴜᴍʙᴇʀ ᴏʀ ʀᴀɴᴅᴏᴍ]
- sᴇᴛ ᴀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ғᴏʀ ᴄʜᴀᴛ. 
"""


ass_num_list = ["1", "2", "3", "4", "5"]


@app.on_message(filters.command(["change", "changeassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**ᴜsᴀɢᴇ:**\n`/changeassistant` [ASS_NO]\n\nsᴇʟᴇᴄᴛ ғʀᴏᴍ ᴛʜᴇᴍ\n{' | '.join(ass_num_list)}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    num = message.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await message.reply_text(usage)
    ass_num = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "ɴᴏ ᴘʀᴇ-sᴀᴠᴇᴅ ᴀssɪsᴛᴀɴᴛ ғᴏᴜɴᴅ...\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ᴀssɪsᴛᴀɴᴛ ᴠɪᴀ /setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(message.chat.id, "assistant", assis)
    await message.reply_text(
        f"**ᴄʜᴀɴɢᴇᴅ ᴀssɪsᴛᴀɴᴛ**\n\nᴄʜᴀɴɢᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ **{ass}** ᴛᴏ ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "5", "Random"]


@app.on_message(filters.command(["set", "setassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**ᴜsᴀɢᴇ:**\n`/setassistant` [ASS_NO or Random]\n\nsᴇʟᴇᴄᴛ ғʀᴏᴍ ᴛʜᴇᴍ\n{' | '.join(ass_num_list2)}\n\nᴜsᴇ 'Random' ᴛᴏ sᴇᴛ ʀᴀɴᴅᴏᴍ ᴀssɪsᴛᴀɴᴛ"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    query = message.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await message.reply_text(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        await message.reply_text(
            f"**__ᴀʟɪsʜᴀ ᴍᴜsɪᴄs ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴀʟʟᴏᴛᴇᴅ__**\n\nᴀssɪsᴛᴀɴᴛ ɴᴏ. **{ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(message.chat.id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"ᴘʀᴇ-sᴀᴠᴇᴅ ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ {ass} ғᴏᴜɴᴅ...\n\nʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ ᴠɪᴀ /changeassistant"
        )


@app.on_message(filters.command("checkassistant") & filters.group)
async def check_ass(_, message: Message):
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "ɴᴏ ᴘʀᴇ-sᴀᴠᴇᴅ ᴀssɪsᴛᴀɴᴛ ғᴏᴜɴᴅ...\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ᴀssɪsᴛᴀɴᴛ ᴠɪᴀ /play"
        )
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"ᴘʀᴇ-sᴀᴠᴇᴅ ᴀssɪsᴛᴀɴᴛ ғᴏᴜɴᴅ\n\n ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ {ass} "
        )
