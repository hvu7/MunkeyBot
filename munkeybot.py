import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
@client.event
async def on_message(message):
	if message.content.startswith('!'):
		await client.send_message(message.channel, 'Hello!')
client.run('MzkzMjkwMjUwMzgzOTE3MDU3.DRznpA.-uud2vwbqHUvPlRI7DgjYt-kh4I')
