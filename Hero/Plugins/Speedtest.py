import os

import speedtest
import wget
from pyrogram import Client, filters
from pyrogram.types import Message

from Hero import BOT_ID, SUDOERS, app
from Hero.Utilities.formatters import bytes

__MODULE__ = "sᴘᴇᴇᴅᴛᴇsᴛ"
__HELP__ = """
`/speedtest`
- ᴄʜᴇᴄᴋ sᴇʀᴠᴇʀ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ sᴘᴇᴇᴅ.
"""


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def statsguwid(_, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅ ᴛᴇsᴛ...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.download()
        m = await m.edit("ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...")
    path = wget.download(result["share"])

    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴘ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴘᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴘɪɴɢ:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
