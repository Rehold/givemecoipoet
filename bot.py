# Imports
import discord
from discord.ext import commands
import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
from os.path import exists as config_exists
import glob
from datetime import datetime
import traceback
config_exists = os.path.exists('config.json')
if config_exists:
    pass
else:
    createconfig = open("config.json", "w")
    json.dump(
        {
            "botToken": "BotToken",
            "database": {
                "mongoUsername": "MongoUsername",
                "mongoPassword": "MongoPassword",
                "mongoHost": "MongoHost",
                "mongoPort": "MongoPort",
                "mongoDatabase": "MongoDatabase"
            },
        },
        createconfig,
    indent=4,
    )
    createconfig.close()


commands_exists = os.path.exists('config.json')
if commands_exists:
    pass
else:
    createcommandsconfig = open("commands.json", "w")
    json.dump(
        {
            "setstatus": "811689415315423282"
        },
        createcommandsconfig,
    indent=4,
    )
    createcommandsconfig.close()
    print(commands_exists)




# Bot subclass
class Buddyv2(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), owner_ids=[842859032628822057, 750470053300011070, 646069031014760448])
        self.uptime = discord.utils.utcnow()
    # Stuff that is run before the bot is ready, best place to load cogs
    async def setup_hook(self):
        await self.load_extension("jishaku") # for debugging
        # custom cog loader that took fucking years to perfect
        for filename in glob.iglob("cogs/**", recursive=True):
            if filename.endswith(".py"):
                try:
                    file = os.path.basename(filename)
                    fn = filename.replace('/', '.').replace('\\', '.').replace(f'.{file}','')
                    cog = f"{fn}.{file.replace('.py', '')}"
                    await self.load_extension(cog)
                    
                    
                except Exception as e:
                    print(e)
                    print(f"Failed to load {cog}")
    
    async def on_ready(self):
     
        await self.tree.sync(
            guild=self.get_guild(811284392156725339)
        )  # Uploads slash commands to discord, guild is specified so we dont have to wait a long ass time


        await bot.change_presence(activity=discord.Activity(name"yes")
        # datetime object containing current date and time for uptime
        uptimeutc = datetime.utcnow()
        uptime = uptimeutc.timestamp()


        print("---------------------------------")
        print("Bot is ready!")
        print("---------------------------------")
# Start the bot
bot = Buddyv2()

bot.run(config["penislover133253"])
