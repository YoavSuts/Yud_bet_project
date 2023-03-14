import discord
import yfinance as yf
from bot_funcs import *
import os


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    msg = message.content.split(" ")
    if message.author == client.user:
        return
    if message.author.id == 351965495655792641:
        await message.channel.send("admin")

    if message.content == "hi":
        await message.channel.send('Hello!')

    elif msg[0] == "stock:":
        market_price = get_current_price(msg[1])
        await message.channel.send(f"{msg[1]} market_price: {market_price}")
    elif msg[0] == "chart:":  # chart: period company
        if len(msg) == 3:
            get_graph(msg[2], msg[1])
            await message.channel.send(file=discord.File(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{msg[2]}.png"))
            os.remove(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{msg[2]}.png")
        elif len(msg) == 2:
            get_graph(msg[1])
            await message.channel.send(file=discord.File(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{msg[1]}.png"))
            os.remove(fr"C:\Cyber_Stock_project\Bot_code\Test_pictures\{msg[1]}.png")








client.run('MTA0ODk0MjE1NjA2MjEzMDI2Nw.GFgzqB.YmqCL-S6GfY8Nr6Of7giDbWyCqU9iR9DpmD9rM')