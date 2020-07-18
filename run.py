import discord
import io
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import random
import time
import requests
import nekos
from discord.ext.commands import has_permissions, CheckFailure
import sys
import os
import string
import argparse

# commited from arch linux belive it or not i know this is mega swagg innit
from colorama import init
## argsparse ###
description = 'A simple bruteforce script that attempts to guess discord server invite codes.'
# Initiate the parser with a description
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-v", "--version",
                    help="show program version", action="store_true")
parser.add_argument("-c", "--commands",
                    help="lists available commands", action="store_true")
args = parser.parse_args()


if args.version:
    print("V1.0")
    exit()

if args.commands:
    print("List of available commands:")
    print("  +guess <amount of guesses to make>")
    print("  +help")
    exit()


###/ARGSPARSE###


init()
# set the preifx and disable the builtin help command that comes with discord.py
client = commands.Bot(command_prefix="+")
client.remove_command("help")


print(Fore.WHITE + "[" + Fore.RED + "+" +
      Fore.WHITE + "]" + "Welcome home, script kiddie")
print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")


@client.event
async def on_ready():
    print("")


@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Color.purple()
    )
    embed.set_author(name="Help")
    embed.add_field(
        name="+help", value='shows this help message', inline=False)
    embed.add_field(
        name="+guess", value='guesses guild invites. usage= +guess (number of guesses.)', inline=False)
    embed.add_field(
        name="Github", value='this discord bots source code is available on github. heres a link:', inline=False)
    embed.add_field(name="+clear", value='clears the console', inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    with io.open("bruhgaming78.txt", "a", encoding="utf-8") as f:
        f.write(
            "[{}] | [{}] | [{}] @ {}: {}\n".format(message.guild, message.channel, message.author, message.created_at,
                                                   message.content))
    f.close()
    print(
        Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + "[{}] | [{}] | [{}] @ {}: {}".format(
            message.guild, message.channel, message.author,
            message.created_at, message.content))

    await client.process_commands(message)


@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://twitch.tv/epic",
                                 name=f"+help | helping {len(client.guilds)} guilds!")
    await client.change_presence(status=discord.Status.idle, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)


# progress bar

def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@client.command()
async def guess(ctx, reason="None"):
    author = ctx.message.author
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author
    items = list(range(0, int(reason)))

# A Nicer, Single-Call Usage
    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    b = int(reason)
    i = 0

    for item in progressBar(items, prefix='Progress:', suffix='Complete', length=50):
        await ctx.send("discord.gg/" + id_generator(6, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"))
        # time.sleep(0.1)

    # while(i < b):
    #   await ctx.send("discord.gg/" + id_generator(6, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"))
    #   i+= 1
        # time.sleep(1)


# clear the console command
@client.command()
async def clear(ctx):
    os.system("clear")
# dummy token in here, well its a dummy now. appearantly discord has a web crawler that found my bots token in here. pretty damn cool.
client.run("NzMxMjU5MzI5NzQyODk3MjA0.Xwmj3w.MmxsRzifBc-WzwIDhRS_ZcIXlWA")

# br
# this is the animation that gets played in case of a crash, error, dyno error etc. if you are running this from windows, i recommend replacing "clear" with "cls" to avoid a visual bug, reminding you that the clear command is unix like only. the t == 3 LOC means the amount of times the animation will repeat before terminating the application.
t = 0
while t != 10:
    print("died")
    time.sleep(1)
    os.system("clear")
    print("died.")
    time.sleep(1)
    os.system("clear")
    print("died..")
    time.sleep(1)
    os.system("clear")
    print("died...")
    time.sleep(1)
    os.system("clear")
    print("died..")
    time.sleep(1)
    os.system("clear")
    print("died.")
    time.sleep(1)
    os.system("clear")
    t += 1
    if(t == 3):
        exit()
