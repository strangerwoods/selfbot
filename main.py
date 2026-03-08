import discord
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            await message.add_reaction('⭐')

client = MyClient()
client.run(os.getenv('TOKEN'))
