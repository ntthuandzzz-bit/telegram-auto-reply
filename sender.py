from telethon.tl.types import Message


class Sender:

    def __init__(self, client):

        self.client = client

    async def send_block(self, chat_id, messages):

        for msg in messages:

            if msg.media:

                await self.client.send_file(

                    chat_id,

                    file=msg.media,

                    caption=msg.text or ""

                )

            elif msg.text:

                await self.client.send_message(

                    chat_id,

                    msg.text

                )
