import discord
import asyncio
import sys
import random
import re
import os
client=discord.Client()

@client.event
async def on_ready():
    print('Welcome message bot Logged in')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """your message
"""

@client.event

async def _on_message(message):
    await client.send_message(member, newUserMessage)

client.run('Nzc1NTg2OTMxNDI0NzU1NzQy.X6ofng.WF6hbqyteX_AbU9e2Nd_HOXmvwE') 
