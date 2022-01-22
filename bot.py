# bot.py
import os
import random
import json
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv


path="C:\Program Files\HandBrake\HandBrake.exe"
ExeToKill="HandBrake.exe"

load_dotenv()
token = os.getenv('CLIENT_TOKEN')
bot = commands.Bot(command_prefix="!")


@bot.event    
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "./startdew":
           member = message.author
           print("caca")
           await message.channel.send('Attempting to start server..')
           os.system('start ""'+' "'+path+'"' )
           await message.channel.send('Server started successfully. Give it just a few seconds to pop-up ingame.')
                
    if message.content == "./stopdew":
           member = message.author
           print("coco")
           await message.channel.send('Attempting to stop server..')
           os.system("TASKKILL /F /IM " +ExeToKill)
           await message.channel.send('Server stopped successfully.')           
    await bot.process_commands(message)
    

bot.run(token)

