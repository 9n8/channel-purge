import discord, os, colorama
import asyncio

from discord.ext import commands
from colorama import Fore, Style

os.system(f'title [PURGER]')
os.system(f'mode 80,20')

token = input(f'{Fore.CYAN}Enter {Fore.LIGHTCYAN_EX}Token:{Fore.GREEN} ')
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')

print(f'                       type sex where u want to purge \n\n')

print(f'                                   {Fore.YELLOW}@pw1337 {Fore.LIGHTMAGENTA_EX} \n')

class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge2"):
            channels=message.channel.guild.channels
        elif(message.content=="sex"):  
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(channel)
            try:
                async for mss in channel.history(limit=None):
                    if(mss.author==self.user):
                        print(mss.content)
                        try:
                            await mss.delete()
                        except:
                            print(f"Can't delete!\n")
            except:
                print("Can't read history!\n")
            

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run(token, bot=False) 