from nextcord.ext import commands

class greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Define a bot command called 'slm'
    @commands.command()
    async def slm(self, ctx):
        await ctx.send("Salut, Fech najem n3awnek?")

    # Define a bot command called 'peace'
    @commands.command()
    async def peace(self, ctx):
        await ctx.send("3la 5ir")

    # When a member joins, the bot gives a message on the same channel
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel  # Get the system channel of the guild
        if channel:
            await channel.send(f"Marhbe bik, {member.mention}")

    # When a member leaves or gets removed, the bot gives a message on the same channel
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel  # Get the system channel of the guild
        if channel:
            await channel.send(f"{member.mention} 5raj min server")
            
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx, num_messages: int):
    # Purge (delete) messages
        await ctx.channel.pu0rge(limit=num_messages + 1)  # +1 to include the command message
        await ctx.send(f"Cleared {num_messages} messages from this channel.")

def setup(bot):
    bot.add_cog(greetings(bot))
