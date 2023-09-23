import nextcord
from nextcord.ext import commands

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help_commands(self,ctx):
        embed = nextcord.Embed(title="Ender Bot Commands",description="9bal kol command tansech bch t7ot -", color=0x800080)
        embed.add_field(name="Audio Commands", value="od5el \no5rej \nsama3ni \nqueue \npause \nkaml \nstop", inline=True)
        embed.add_field(name="Greetings Commands", value="slm \n peace\n chkun_enti \n welcome", inline=True)
        embed.add_field(name="Admins Commands", value="add_role \n remove_role \n ban \n unban \n kick \nclear", inline=True)
        await ctx.send(embed=embed)

    # Create an Embed (which is not necessary at the moment)
    @commands.command()
    async def chkun_enti(self, ctx):
        embed = nextcord.Embed(title="Ender", description="Your Favorite Discord Bot", color=0x800080)
        embed.set_author(name=ctx.author.display_name, icon_url="https://ih1.redbubble.net/image.2243757246.7180/gbrf,10x10,f,540x540-pad,450x450,f8f8f8.jpg")
        # embed.add_field(name="", value="", inline=True)
        await ctx.send(embed=embed)

    # Send an embedded message to new members
    @commands.command()
    async def welcome(self, ctx, user: nextcord.Member, *, message=None):
        message = f"Mar7be bik fi {ctx.guild.name} {user.name}"
        embed = nextcord.Embed(title=message, color=0x800080)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(embeds(bot))
