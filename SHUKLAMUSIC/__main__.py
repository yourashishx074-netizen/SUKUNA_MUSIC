# --------------- ADD THESE IMPORTS AT THE TOP ---------------
import os
from aiohttp import web
# -----------------------------------------------------------

import asyncio
import importlib
from pyrogram import idle
from pygcals.exceptions import NoActiveGroupCall
import config
from SHUKLAMUSIC import LOGGER, app, userbot
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.misc import sudo
from SHUKLAMUSIC.plugins import ALL_MODULES
from SHUKLAMUSIC.utils.database import get_banned_users, get_gbanned

# --------------- ADD THIS WEB SERVER FUNCTION ---------------
async def web_server():
    async def handle(request):
        return web.Response(text="Bot is running!")
    
    app_web = web.Application()
    app_web.router.add_get("/", handle)
    runner = web.AppRunner(app_web)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
# -----------------------------------------------------------

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("String Session Not Filled, Please Fill A Pyrogram Session")
        exit()
    
    # --------------- START THE WEB SERVER HERE ---------------
    await web_server()
    # ---------------------------------------------------------

    await sudo()
    try:
        users = await get_banned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_gbanned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    
    await app.start()
    for all_module in ALL_MODULES:
        import_module(f"SHUKLAMUSIC.plugins.{all_module}")
    LOGGER("SHUKLAMUSIC.plugins").info("All Features Loaded Safe..")
    await userbot.start()
    await SHUKLA.start()
    try:
        await SHUKLA.stream_call("https://te.legra.ph/file/20f784e49d230ab62e9s.mp4")
    except NoActiveGroupCall:
        LOGGER("SHUKLAMUSIC").error(
            "[!] - PLZ START YOUR LOG GROUP VOICECHAT/CHANNEL..\n\nSTRANGER BOT STOP......"
        )
        exit()
    except:
        pass
    
    await SHUKLA.decorators()
    LOGGER("SHUKLAMUSIC").info(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    )
    LOGGER("SHUKLAMUSIC").info(
        f"[?] ~~~~~~~~ » [ MADE BY MR SHIVANSH ] ~~~~~~~~ [?]"
    )
    LOGGER("SHUKLAMUSIC").info(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    )
    
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SHUKLAMUSIC").info("STOP STRANGER MUSIC BOT..")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    
