# oracle_discord_bot.py
# pip3 install python-dotenv discord.py
# .env
# DISCORD_TOKEN=<YOURTOKEN>

import os
import requests

import discord
from dotenv import load_dotenv

from web3 import Web3
import json

import time
import decimal

#Input Token Priced against Stable
inputToken = "27G8MtK7VtTcCHkpASjSDdkWWYfoqT6ggEuKidVJidD4"
outputToken = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
amountIn = "1000000"

#Priced against SOL
outputNativeToken = "So11111111111111111111111111111111111111112"
amountInputIn = "1000000"
decimalsNative = 1000000000
decimalsStable = 1000000
decimalsToken = 1000000

url = "https://quote-api.jup.ag/v6/quote?outputMint="+outputToken+"&inputMint="+inputToken+"&amount="+amountIn+"&slippage=0.2"
urlNative = "https://quote-api.jup.ag/v6/quote?outputMint="+outputNativeToken+"&inputMint="+inputToken+"&amount="+amountInputIn+"&slippage=0.2"

payload = {}
headers = {
  'Accept': 'application/json'
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_JUPITER_JLP')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        for guild in client.guilds:
        #while True:

            response = requests.request("GET", url, headers=headers, data=payload)
            responseNative = requests.request("GET", urlNative, headers=headers, data=payload)
            #print(response.text)
            #print(response.json())

            responsePrice = json.dumps(response.json())
            resp = json.loads(responsePrice)
            priceValue = (resp['outAmount'])
            finalValue = decimal.Decimal(priceValue)/decimalsStable
            print(finalValue)

            responsePriceNative = json.dumps(responseNative.json())
            respNative = json.loads(responsePriceNative)
            priceValueNative = (respNative['outAmount'])
            finalValueNative = decimal.Decimal(priceValueNative)/decimalsNative
            print(finalValueNative)
          
            botPrice = "JLP $" + str(finalValue)
            botPriceNative = "SOL " + str(finalValueNative)

            await guild.me.edit(nick=botPrice)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=botPriceNative ))
         #   time.sleep(5)
            time.sleep(10)

client.run(TOKEN)
