from discord.ext import commands
import discord
import scraper
import csv
import datetime



BOT_TOKEN = "MTE0NTczMTQ2ODU1NTk5MzEwOA.GEUDXb.jcP-jzKfJxsf4-8dwFxkg5eomZR3yQHDh-mXJg"
CHANNEL_ID = 1145769276045803531

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

bot.remove_command('help')

def update_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        csv_writer.writerow([timestamp, data])


@bot.event
async def on_ready():
   print("Crickey is waiting!")
   channel = bot.get_channel(int(CHANNEL_ID))  
   await channel.send("Crickey is waiting")

@bot.command()
async def help(ctx):
    help_message = (
        "```"
        "Bot Commands:\n"
        "/livescore - Get the current live cricket score.\n"
        "/generate - Generate a CSV file with previous live scores.\n"
        "/help     - Information about the commands.\n"
        "\n"
        "Usage:\n"
        "Use /command to execute a command."
        "```"
    )
    
    await ctx.send(help_message)

   


@bot.command()
async def livescore(ctx):
   score_info = scraper.fetch_live_score()

   if score_info:
        update_csv("live_scores.csv", score_info)
        await ctx.send(score_info)
   else:
       await ctx.send("No live matches currently. No livescores available.")

@bot.command()
async def generate(ctx):
    try:
        with open("live_scores.csv", 'rb') as csvfile:
            await ctx.send(file=discord.File(csvfile, "live_scores.csv"))
    except FileNotFoundError:
        await ctx.send("No CSV file")






bot.run(BOT_TOKEN)
