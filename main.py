import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(discord.Client):

	async def on_ready(self):
		print(f'Logged on as {self.user}!')
		self.scheduled_task.start()

	@tasks.loop(hours=24)
	async def scheduled_task(self):
		channel = self.get_channel(int(os.getenv('PERSONAL_CHANNEL')))
		if channel:
			# Fetch slash commands in the channel
			app_commands = await channel.application_commands()

			TARGET_BOT_ID = int(os.getenv('TARGET_BOT_ID'))

			command = next((cmd for cmd in app_commands if cmd.name == "daily" and cmd.application_id == TARGET_BOT_ID), None)

			if command:
				await command(channel=channel)
			else:
				print("Command not found")


	async def on_message(self, message):
		if message.author != self.user:
			return  # Ignore the bot's own messages

		if message.content.startswith('$update'):
			await message.delete()
			await message.channel.send('New post is up!')

		await message.add_reaction('⭐')

client = MyClient()
client.run(os.getenv('TOKEN'))
