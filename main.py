import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
STRING_SESSION = os.environ["STRING_SESSION"]

AUTO_REPLY = os.getenv(
    "AUTO_REPLY",
    "👋 Xin chào!\n\nMình đã nhận được tin nhắn của bạn.\nHiện mình đang bận nên chưa thể trả lời ngay.\nVui lòng để lại nội dung, mình sẽ phản hồi sớm."
)

client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)

replied = set()

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return

    sender = await event.get_sender()

    if sender.bot:
        return

    if sender.contact:
        return

    if sender.id in replied:
        return

    await event.reply(AUTO_REPLY)
    replied.add(sender.id)

async def main():
    print("✅ Userbot started")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
