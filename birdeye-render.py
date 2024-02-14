# birdeye-render.py
# pip3 install python-dotenv discord.py
# nano .env
# DISCORD_TOKEN_BIRDEYE_RENDER=<YOURTOKEN>

import os
import requests

import discord
from dotenv import load_dotenv

from web3 import Web3
import json

import time
import decimal

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_BIRDEYE_RENDER')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        for guild in client.guilds:
        #while True:
            url = "https://public-api.birdeye.so/public/price?address=rndrizKT3MK1iimdxRdWabcF7Zg7AR5T4nud4EkHBof"
            urlToken = "https://public-api.birdeye.so/public/price?address=So11111111111111111111111111111111111111112"
            headers = {"X-API-KEY": "<BIRDEYE-APIKEY>"}
            response = requests.get(url, headers=headers)
            responseToken = requests.get(urlToken, headers=headers)

            print(response.json())
            print(responseToken.json())

            responsePrice = json.dumps(response.json())
            resp = json.loads(responsePrice)
            priceValue = (resp['data']['value'])
            convertValue = str(priceValue)

            responsePriceToken = json.dumps(responseToken.json())
            respToken = json.loads(responsePriceToken)
            priceValueToken = (respToken['data']['value'])
            convertValueToken = str(priceValueToken)

            #birdEyePrice = "BONK " + str(round((response), 6))
            birdEyePrice = "RENDER " + str(convertValue)
            convertSol = decimal.Decimal(convertValue)/decimal.Decimal(convertValueToken)
            birdEyePriceToken = "SOL " + str(convertSol)

            await guild.me.edit(nick=birdEyePrice)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=birdEyePriceToken ))
            time.sleep(15)

client.run(TOKEN)
