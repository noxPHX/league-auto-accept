from discord import Client


class DiscordBot(Client):

    def __init__(self, queue, channel_id):
        super(DiscordBot, self).__init__()
        self.queue = queue
        self.channel_id = channel_id

    async def on_ready(self):
        print(f'{self.user} is ready, waiting...')
        match = self.queue.get()
        await self.get_channel(self.channel_id).send(match)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'A':
            self.queue.put("ACCEPT")
        else:
            self.queue.put("DECLINE")


async def start(queue, token, channel_id):
    await DiscordBot(queue, channel_id).start(token)


def run_it_forever(loop):
    loop.run_forever()
