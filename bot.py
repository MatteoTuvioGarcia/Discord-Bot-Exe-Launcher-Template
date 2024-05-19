# bot.py
import os
import rcon
import cv2  as cv  
import discord
from discord import Intents
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
import os
# from paho.mqtt import client as mqtt_client
# import random
# broker = 'broker.emqx.io'
# port = 1883
# topic = "python/mqtt"
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'MQTTusr'
# password = 'XuCpHrA'

# def connect_mqtt():
#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to MQTT Broker!")
#         else:
#             print("Failed to connect, return code %d\n", rc)

#     client = mqtt_client.Client(client_id)
#     client.username_pw_set(username, password)
#     client.on_connect = on_connect
#     client.connect(broker, port)
#     return client

# client = connect_mqtt()
# client.loop_start()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
RCON_PASS = os.getenv('RCON_PASS')
bot = commands.Bot(command_prefix='!',intents=Intents().all())

async def send_rcon(rconCommand):
    response = await rcon.source.rcon(
    rconCommand,
    host='localhost', port=25575, passwd=RCON_PASS
    )
    response = response.replace("§e", "")
    response = response.replace("§f", "")
    response = response.replace("§6", "")
    response = response.replace("§7", "")
    return response

@bot.command(name='list', help="Displays a list of currently connected players.")
async def list(ctx):
    response = await send_rcon('list')
    await ctx.send(response)

@bot.command(name='kick', help="kicks a user, for shits and giggles.")
@has_permissions(administrator=True)  
async def kick(ctx, user = ""):
    if user == "":
        await ctx.send("You must choose a user to kick.")
        return
    response = await send_rcon('kick ' + user)
    await ctx.send(response)

@bot.command(name='start', help="Starts up the server.")
@has_permissions(administrator=True)  
async def start(ctx):
    response = os.system("sudo systemctl start minecraft")
    await ctx.send(response)

@bot.command(name='stop', help="Stops the server.")
@has_permissions(administrator=True)  
async def stop(ctx):
    response = await send_rcon('stop')
    await ctx.send(response)

@bot.event
async def on_message(message):
    print(message.content)
    
@bot.command(name='snap', help="This is literally privacy invasion")
@has_permissions(administrator=True)  
async def snap(ctx):
    apiID = cv.CAP_DSHOW
    cam = cv.VideoCapture(0,apiID)
    if not cam.isOpened():
        response = "Cannot open camera"
        await ctx.send(response)
    else:
        ret, frame = cam.read()
        filename = 'savedImage.jpg'
        cv.imwrite(filename, frame) 
        await ctx.send(file=discord.File(filename))
    
@start.error
@stop.error
async def permError(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("👉🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👈🏿 \n"+
                        "👉🏿👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👈🏿\n" +
                        "👉🏿👉🏾👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👉🏽👇🏼👇🏼👇🏼👇🏼👇🏼👈🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👉🏽👉🏼👇🏻👇🏻👇🏻👈🏼👈🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👉🏽👉🏼👉🏻🤓👈🏻👈🏼👈🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👉🏽👉🏼👆🏻👆🏻👆🏻👈🏼👈🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👉🏽👆🏼👆🏼👆🏼👆🏼👆🏼👈🏽👈🏾👈🏿\n" +
                        "👉🏿👉🏾👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👈🏾👈🏿\n" +
                        "👉🏿👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👈🏿\n" +
                        "👉🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👈🏿\n")
        await ctx.send("Nice try, kitten. Come back when you're an admin and a discord mod :rage:")


bot.run(TOKEN)

