# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv

# ____________________CONFIG_AREA_____________________________#

path = "C:/Program Files/HandBrake/HandBrake.exe"
ExeToKill = "HandBrake.exe"
prefix = "!"
# ____________________CONFIG_AREA_____________________________#

print("hello")
load_dotenv()
token = os.getenv('CLIENT_TOKEN')
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == prefix + "start":
        print("chkpnt")
        await message.channel.send('Attempting to start server..')
        os.system('start ""' + ' "' + path + '"')
        await message.channel.send('Server started successfully. Give it just a few seconds to pop-up ingame.')

    if message.content == prefix + "stop":
        print("chkpnt2")
        await message.channel.send('Attempting to stop server..')
        os.system("TASKKILL /F /IM " + ExeToKill)
        await message.channel.send('Server stopped successfully.')
    await bot.process_commands(message)


bot.run(token)
