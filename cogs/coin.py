from random import randint
import asyncio
import datetime
from discord.ext import commands

# Followers of the Crafting Table #general id: 614889263196143742
# Followers of the Crafting Table Guild id: 614889263183560840

class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.default_guild_id = 614889263183560840 
        self.default_channel_id = 614889263196143742 # these vars are to be used as placeholders before there are universal channels - Tasni/BTMI
    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        """Randomly gives money to active members."""
        random_ct_int = randint(1, 250)
        if not message.author.bot and random_ct_int == 250:
            user_id = str(message.author.id)

            if user_id not in self.bot.coin:
                self.bot.coindb[user_id] = 0
            self.bot.coindb[user_id] += 1

            await message.channel.send(
                message.author.id + ", you just earned a crafting table!"
            )
            self.bot.save_coindb()
            
def setup(bot):
    bot.add_cog(Coin(bot))
