
import logging
import threading
import os
import asyncio
from xml.etree.ElementTree import tostring
import discord
from dotenv import load_dotenv
import socketio

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
sio = socketio.AsyncClient()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startWith == '/help':
        await message.channel.send()

    if message.content.startWith == '/list-contracts':
        await message.channel.send()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def connect():
    await sio.connect('ws://api.diadata.org/ws/nft')
    await sio.wait()

def run_websocket():
    pass

def run_discord():
    client.run(TOKEN)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # b = threading.main_thread(target=run_discord)
    # b.start()
    a = threading.Thread(target=asyncio.run(connect()))
    a.start()
    