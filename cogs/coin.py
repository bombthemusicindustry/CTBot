import json
from random import randint

from discord.ext import commands


class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        with open('./data/coindb.json') as c:
            coindb = json.load(c)
        user_id = str(message.author.id)
        if user_id not in coindb:
            coindb[user_id] = 0
        randomctint = randint(1, 250)
        if randomctint == 250:
            coindb[user_id] += 1
            await message.channel.send(message.author.id + ", you just earned a crafting table!")
            with open('./data/coindb.json', 'w') as d:
                json.dump(coindb, d, indent=2)


def setup(bot):
    bot.add_cog(Coin(bot))
