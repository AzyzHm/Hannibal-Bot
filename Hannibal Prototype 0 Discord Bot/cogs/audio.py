from nextcord.ext import commands
from nextcord import FFmpegPCMAudio

class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}

    # join the voice chat
    @commands.command(pass_context=True)
    async def od5el(self, ctx):
        if ctx.author.voice:  # Check if the author is in a voice channel
            channel = ctx.author.voice.channel
            voice_client = ctx.voice_client
            if voice_client:  # Check if the bot is already in a voice channel
                await voice_client.move_to(channel)  # Move to the author's channel
            else:
                await channel.connect()  # Connect to the author's channel
        else:
            await ctx.send("Lezem tkoun fi voice chat!!")

    # leave the voice chat
    @commands.command(pass_context=True)
    async def o5rej(self, ctx):
        voice_client = ctx.voice_client
        if voice_client:  # Check if the bot is in a voice channel
            await voice_client.disconnect()  # Disconnect from the voice channel
            await ctx.send("Ani 5rajt mil voice chat")
        else:
            await ctx.send("Menich fil voice chat!!")

    # pauses an audio
    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice = ctx.voice_client
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Mafamma 7atta song 9a3da tmchi tw!")

    # continue playing an audio
    @commands.command(pass_context=True)
    async def kaml(self, ctx):
        voice = ctx.voice_client
        if voice and voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Mafama 7atta song en pause!")

    # stops playing an audio
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        voice = ctx.voice_client
        if voice and (voice.is_playing() or voice.is_paused()):
            voice.stop()
        else:
            await ctx.send("Mafmma 7atta song 9a3da temchi")

    # play a given audio
    @commands.command(pass_context=True)
    async def sama3ni(self, ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(arg)
        player = voice.play(source, after=lambda x=None: self.check_queue(ctx, ctx.message.guild.id))

    def check_queue(self, ctx, id):
        if self.queues.get(id):
            voice = ctx.guild.voice_client
            source = self.queues[id].pop(0)
            player = voice.play(source)

    # queue an audio
    @commands.command(pass_context=True)
    async def queue(self, ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(arg)
        guild_id = ctx.message.guild.id

        if guild_id in self.queues:
            self.queues[guild_id].append(source)
        else:
            self.queues[guild_id] = [source]
            await ctx.send("Added to Queue !")

def setup(bot):
    bot.add_cog(audio(bot))
