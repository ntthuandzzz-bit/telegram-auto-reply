from telethon import TelegramClient, events
from telethon.tl.types import User
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

AUTO_REPLY = """👋 Xin chào!

Mình đã nhận được tin nhắn của bạn.

Hiện mình chưa thể trả lời ngay. Vui lòng để lại nội dung, mình sẽ phản hồi sớm nhất.
"""

replied = set()

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if not event.is_private:
        return

    sender = await event.get_sender()

    if not isinstance(sender, User):
        return

    if sender.bot:
        return

    if sender.contact:
        return

    if sender.id in replied:
        return

    await event.reply(AUTO_REPLY)
    replied.add(sender.id)

client.start()
print("Userbot is running...")
client.run_until_disconnected()
