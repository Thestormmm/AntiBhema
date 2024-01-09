import os
import discord
from discord.ext import commands
from dotenv import main

main.load_dotenv(dotenv_path="config")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '!', intents= intents)

@bot.event
async def on_ready():
    print("AntiWabna is ON !")

@bot.command(name='thisissparta')
async def move_to(ctx):
    guild_id = 638815365807472680
    guild = bot.get_guild(guild_id)

    if guild:
        target_id = 1193533055982370839
        target = guild.get_member(target_id)

        if target:
            await ctx.send(f'Ya {target.display_name} Ya miboun !!      ')
            await target.move_to(None)
        else:
            await ctx.send('User not found in the guild.')
    else:
        await ctx.send('Bot is not in the specified guild or the guild ID is incorrect.')


bot.run(os.getenv("TOKEN")) # type: ignores
