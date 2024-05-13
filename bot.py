from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "14050586"))
API_HASH = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "SongsDownloaderTgBot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
