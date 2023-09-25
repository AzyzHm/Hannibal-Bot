import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions

with open('Profanity.txt','r') as file:
    Tn_profanity = [line.strip() for line in file]

class Integrity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Detect Bad messages and delete them
    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if the message is from a bot or the author is the bot itself to prevent infinite loops
        if message.author.bot or message.author == self.bot.user:
            return

        for word in Tn_profanity:
            if word in message.content:
                await message.delete()
                await message.channel.send("Ay kelma zeyda tnajem tetbana 3leha!")
                return  # Stop processing the message further if it contains an offensive word
        if "bot tell me a joke" in message.content.lower():
            await message.channel.send("Inti Tounsi HAHAHAHAHAHA!!")
        if ("mechi nofter" in message.content) or ("kont nofter" in message.content):
            await message.channel.send("sa7a w bechfee")
        if("gg" in message.content.lower()) or ("gj" in message.content.lower()):
            await message.channel.send("GG Guys")
        if "hannibal" in message.content.lower():
            await message.channel.send("Kenek 7ajtek beya w ma3raftech lcommands type `-help_commands`")
        if "shinhi" in message.content.lower():
            await message.channel.send("shinhi li shinhi?")
        if "barra mrigl" in message.content.lower():
            await message.channel.send("Barra Mrigl!!")
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command mouch mawjouda, type`-help_commands` bch tchouf les commands")
    # Kick a member
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Aya 3la5ir {member} tza3ek min server")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Ma3andekch Permission bch t3mel Kick lmember e5er !!")

    # Ban a member
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Aya 3la5ir\n{member} tbana min server")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Ma3andekch Permission bch t3mel ban lmember e5er !!")

    # UnBan a member
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, member: nextcord.Member, *, reason=None):
        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            if user.id == member.id:
                await ctx.guild.unban(user, reason=reason)
                await ctx.send(f"{user.mention} bl3 ban!")
                return

        await ctx.send(f"{user.mention} mahouch me5ou ban!")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Ma3andekch permission bch tna7i ban!")

    # Add Role
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def add_role(self, ctx, user: nextcord.Member, *, role: nextcord.Role):
        if role in user.roles:
            await ctx.send(f"{user.mention} c'est deja {role}")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")
            
    @add_role.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("ma3andekch Permission")
            
    # Remove Role
    @commands.command(pass_context=True)
    @has_permissions(manage_roles=True)
    async def remove_role(self, ctx, user: nextcord.Member, *, role: nextcord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"{user.mention} ma3adech {role}")
        else:
            await ctx.send(f"{user.mention} C'est deja mahouch {role}")
            
    @remove_role.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("ma3andekch Permission")
    #clear command
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx, num_messages: int):
    # Purge (delete) messages
        await ctx.channel.purge(limit=num_messages + 1)  # +1 to include the command message
        await ctx.send(f"Cleared {num_messages} messages from this channel.")
    
    # Most a Active Member
    @commands.command()
    async def most_active(self, ctx):
        # Initialize variables to store the most active member and their message count
        most_active_member = None
        max_message_count = 0

        # Iterate through all members in the server
        for member in ctx.guild.members:
            # Check if the member is a bot (you can exclude bots if you want)
            if member.bot:
                continue

            # Get the message count of the member
            message_count = sum(1 for message in await ctx.channel.history().filter(lambda m: m.author == member).flatten())

            # Update the most active member if this member has more messages
            if message_count > max_message_count:
                max_message_count = message_count
                most_active_member = member

        if most_active_member:
            await ctx.send(f"{most_active_member.mention} Howa akther we7ed active fil server!")
        else:
            await ctx.send("Mafamma 7atta we7ed active (lotf ya rabi)")  

def setup(bot):
    bot.add_cog(Integrity(bot))
