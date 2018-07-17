import discord
from discord import Embed

import SECRETS
import asyncio as asyncio

from commands import cmd_ping, STATICS, cmd_wisdom, cmd_dice, cmd_horn

print("RDA - DiscordBotSoftware by SunRobinDev started.")

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "wisdom": cmd_wisdom,
    "dice": cmd_dice,
    "horn": cmd_horn
}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot logged in successfully")
    for s in client.servers:
        print((" - %s (%s)" % (s.name, s.id)))
    yield from client.change_presence(game=discord.Game(name="This is just a test"))


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("INVOKE: %s \nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'", " ")))
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke)
        else:
            yield from client.send_message(message.author, embed=Embed(color=discord.Color.red(), description=("The command '%s' is not valid " % invoke)))


client.run(SECRETS.token)
