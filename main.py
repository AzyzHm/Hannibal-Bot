import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="-", intents=nextcord.Intents.all())
@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game("With Your Mind"))
    setup_hook()
    print("The bot is now ready for use !")

def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded Cog: {filename[:-3]}")
      
if __name__ == "__main__":
    token = os.getenv('TOKEN')

if token:
    bot.run(token)
else:
    print("Bot token not found. Please set the TOKEN environment variable in the .env file.")
