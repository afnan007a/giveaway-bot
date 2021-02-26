import discord
from discord.ext import commands
import datetime
import asyncio
import random

client=commands.Bot(command_prefix="-")
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle,activity=discord.Game('Python'))
	print("the bot is ready")

@client.command()
@commands.has_role("Owner")
async def giveaway(ctx,mins:int,*,prize:str):
    embed=discord.Embed(title="Giveaway!", description=f"{prize}",color=ctx.author.color)

    end=datetime.datetime.utcnow()+datetime.timedelta(seconds=mins*60)

    embed.add_field(name="Ends At:",value=f"{end}UTC")
    embed.set_footer(text=f"Ends {mins} minutes from now!")

    my_msg=await ctx.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins*60)

    new_msg=await ctx.channel.fetch_message(my_msg.id)

    users= await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner=random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")


client.run("YOUR TOKEN")
