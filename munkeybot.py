import discord
import asyncio
import random
import pickle
import os

client = discord.Client()
client.login("MzYyNzg0MTkwNTEwNTMwNTYw.DK3s5Q.OgAO_J3iPi7zvHa4IMvvFwD957g");

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)

	
@client.event
async def on_message(message):
	if message.content.startswith('!'):
		await client.send_message(message.channel, 'Hello!')
client.run('MzkzMjkwMjUwMzgzOTE3MDU3.DRznpA.-uud2vwbqHUvPlRI7DgjYt-kh4I')
#client.run("MzYyNzg0MTkwNTEwNTMwNTYw.DK3s5Q.OgAO_J3iPi7zvHa4IMvvFwD957g");