import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('Please, enter the voice channel')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
        ctx.voice_client.stop()
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn',
            'executable': r'F:\python\ffmpeg\bin\ffmpeg.exe'
        }
        ytdl_options = {
            'format': 'bestaudio/best',
            'quiet': True,
            'default_search': 'auto'
        }
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
            info = ytdl.extract_info(url, download=False)
            audio_url = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(audio_url, **ffmpeg_options)
            vc.play(source)
