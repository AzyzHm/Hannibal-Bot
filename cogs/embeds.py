import nextcord
from nextcord.ext import commands

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # help command
    @commands.command()
    async def help_commands(self,ctx):
        embed = nextcord.Embed(title="Hannibal Bot Commands",description="Note : command sama3ni t5adm ken Song.mp3 or Song2.mp3 5ater bot mazel under development", color=0x008080)
        embed.add_field(name="Audio Commands", value="od5el \no5rej \nsama3ni \nqueue \npause \nkaml \nstop", inline=True)
        embed.add_field(name="Greetings Commands", value="slm \n peace\n chkun_enti \n welcome", inline=True)
        embed.add_field(name="Admins Commands", value="add_role \n remove_role \n ban \n unban \n kick \nclear \nmost_active", inline=True)
        await ctx.send(embed=embed)

    # Create an Embed (which is not necessary at the moment)
    @commands.command()
    async def chkun_enti(self, ctx):
        embed = nextcord.Embed(title="Hannibal", description="Bot Tounsi mzel under development", color=0x008080)
        # embed.add_field(name="", value="", inline=True)
        await ctx.send(embed=embed)

    # Send an embedded message to new members
    @commands.command()
    async def welcome(self, ctx, user: nextcord.Member, *, message=None):
        message = f"Mar7be bik fi {ctx.guild.name} {user.name}"
        embed = nextcord.Embed(title=message, color=0x008080)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(embeds(bot))

def setup(bot):
    bot.add_cog(embeds(bot))
