# Imports
from time import perf_counter
import discord
from discord.ext import commands
from discord import app_commands 
import json
# Cog subclass
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Allows us to use the bot outside of the __init__ function
        self.bot.tree.add_command(ping) # Register the slash command in our bot

#note!! need to change to cmd groups
@app_commands.command(name="ping", description="Get the latency of the bot.")
@app_commands.guilds(811284392156725339) 
async def ping(interaction: discord.Interaction):
    #code
    start = perf_counter()
    await interaction.client.database.db.command('ping')
    end = perf_counter()
    dblatency = end - start
    embed=discord.Embed(title=":ping_pong: Pong!", colour=0x33ECFF)
    embed.add_field(name="• Bot latency:", value=f"{round(interaction.client.latency * 1000)}ms")
    embed.add_field(name="• Database latency:", value=f"{round(dblatency * 1000)}ms")
    await interaction.response.send_message(embed=embed)

# Sets up the cog
async def setup(bot):
    await bot.add_cog(Ping(bot))
