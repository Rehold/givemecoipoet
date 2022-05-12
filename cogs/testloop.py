# Imports
from time import perf_counter
import discord
from discord.ext import commands
from discord import app_commands 
import json
from discord.ext import tasks
# Cog subclass
class Events1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Allows us to use the bot outside of the __init__ function
    async def cog_load(self):
        self.loop_thing.start()
    async def cog_unload(self):
        self.loop_thing.cancel()
    
    @tasks.loop(minutes=1)
    async def loop_thing(self):
        print("Loop thing has executed")
        


 #Sets up the cog
async def setup(bot):
    await bot.add_cog(Events1(bot)) 
