from telethon.tl.types import Message

class BlockParser:

    def __init__(self, client, channel_id):

        self.client = client
        self.channel_id = channel_id

        self.blocks = {}

    async def reload(self):

        self.blocks.clear()

        current = None

        async for msg in self.client.iter_messages(
            self.channel_id,
            reverse=True
        ):

            if not isinstance(msg, Message):
                continue

            text = msg.raw_text or ""

            if text.startswith("#BLOCK"):

                args = text.split()

                if len(args) < 2:
                    continue

                name = args[1].lower()

                self.blocks[name] = []

                current = name

                continue

            if current is None:
                continue

            self.blocks[current].append(msg)

    def exists(self, name):

        return name.lower() in self.blocks

    def names(self):

        return sorted(self.blocks.keys())

    def get(self, name):

        return self.blocks.get(name.lower(), [])
