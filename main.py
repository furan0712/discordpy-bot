# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if ("①"and "⑤"and "⑥" in message.content):
        verify_channel = 1084418616386142258
        if message.channel.id != verify_channel:
            return
        role_verify = 1034398254189793300
        guild = client.get_guild
        member = message.author
        role = member.guild.get_role(role_verify)
        await member.add_roles(role)
        


client.run(os.environ["DISCORD_TOKEN"])
