from telethon import TelegramClient
from telethon.sessions import StringSession

from config import *
from database import Database

db = Database(DATABASE_NAME)

if db.get_setting("enabled") is None:
    db.set_setting("enabled", "1")

if db.get_setting("current_block") is None:
    db.set_setting("current_block", DEFAULT_BLOCK)

client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)


async def startup():

    me = await client.get_me()

    print("=" * 50)
    print("Telegram Auto Reply V2")
    print("=" * 50)
    print(f"User      : {me.first_name}")
    print(f"Username  : @{me.username}")
    print(f"User ID   : {me.id}")
    print(f"Current   : {db.get_setting('current_block')}")
    print("=" * 50)


async def main():

    await startup()

    print("Userbot Started.")

    await client.run_until_disconnected()


with client:
    client.loop.run_until_complete(main())
