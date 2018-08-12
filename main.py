import discord
from discord import Embed

import SECRETS
import langfile
import asyncio as asyncio

#import commandfiles
from commands import cmd_ping, STATICS, cmd_wisdom, cmd_dice, cmd_horn, cmd_gamingsong, cmd_chartsong, cmd_moep, cmd_jaaa, cmd_rapsong, cmd_nightcore, cmd_metalsong, cmd_rocksong, cmd_twitterflw

print("RDA - DiscordBotSoftware by SunRobinDev started.") #start message

client = discord.Client() #register new client

#register commands
commands = {

    "ping": cmd_ping,
    "wisdom": cmd_wisdom,
    "dice": cmd_dice,
    "horn": cmd_horn,
    "gamingsong": cmd_gamingsong,
    "chartsong": cmd_chartsong,
    "moep": cmd_moep,
    "jaaa": cmd_jaaa,
    "rapsong": cmd_rapsong,
    "nightcore": cmd_nightcore,
    "metalsong": cmd_metalsong,
    "rocksong": cmd_rocksong,
    "twitterflw": cmd_twitterflw

}


#async def when bot is connected
@client.event
@asyncio.coroutine
def on_ready():
    print(lang_login)
    for s in client.servers:
        print((" - %s (%s)" % (s.name, s.id)))
    yield from client.change_presence(game=discord.Game(name="sunrobindev.de")) #set status

#commandparser
@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX): #check for invoke
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0] #parse the command
        args = message.content.split(" ")[1:]
        print("INVOKE: %s \nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'", " ")))
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke) #call execution def of commandfiles
        else:
            yield from client.send_message(message.author, embed=Embed(color=discord.Color.red(), description=("The command '%s' is not valid " % invoke))) #message when invalid command is issued


client.run(SECRETS.token) #start client
