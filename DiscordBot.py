from discord import Client
from discord.ext import tasks
from queue import Empty


class DiscordBot(Client):

    def __init__(self, queue, channel_id):
        super(DiscordBot, self).__init__()
        self.queue = queue
        self.channel_id = int(channel_id)

    async def on_ready(self):
        print(f'{self.user} is ready, waiting...')
        await self.get_channel(self.channel_id).send("Ready to feed!")
        self.on_match.start()

    @tasks.loop(seconds=0.5)
    async def on_match(self):
        try:
            match = self.queue.get(False)
        except Empty:
            return
        await self.get_channel(self.channel_id).send(match)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'A':
            self.queue.put("ACCEPT")
            await self.get_channel(self.channel_id).send("Prepare yourself!")
        else:
            self.queue.put("DECLINE")
            await self.get_channel(self.channel_id).send("Not today!")


async def start(queue, token, channel_id):
    await DiscordBot(queue, channel_id).start(token)
