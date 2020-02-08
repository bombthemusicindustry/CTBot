import asyncio
import json
import traceback
from os import path

import discord
from discord.ext import commands
from discord.ext.commands import ExtensionError

from utils import checks


class CTBot(commands.Bot):
    def __init__(self, **options):
        if path.isfile('data/coindb.json'):
            with open('data/coindb.json') as f:
                self.coindb = json.load(f)
        else:
            with open('data/coindb.json', 'w') as f:
                json.dump({}, f, ensure_ascii=False)

        with open('config/config.json') as f:
            self.config = json.load(f)

        super().__init__(self.config['prefix'], activity=discord.Game(name='Back Online'), **options)

        self.remove_command('help')

    def save_coindb(self):
        with open('data/coindb.json', 'w') as f:
            json.dump(self.coindb, f, ensure_ascii=False)

    def run(self):
        super().run(self.config['token'])

    async def reload(self):
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game(name='Reloading'))
        for ext in self.extensions:
            print(f"Reloading {ext}...")
            self.reload_extension(ext)
        await self.change_presence(status=discord.Status.online, activity=discord.Game(name='Back Online'))


bot = CTBot(case_insensitive=True)
initial_extensions = [
    'autoresponse', 'core', 'error_handler', 'lockdown', 'appeals', 'dev', 'coin', 'moderation', 'censor'
]
errors = []


async def status_task():
    activities = bot.config['activities']
    while True:
        for activity in activities:
            await asyncio.sleep(15)
            await bot.change_presence(activity=discord.Activity(name=activity['name'],
                                                                type=discord.ActivityType[activity['status']]))


@bot.event
async def on_ready():
    bot.server = bot.get_guild(bot.config['server'])
    bot.loop.create_task(status_task())
    print('Logged in as', bot.user, "with user id", bot.user.id)
    channel = bot.get_channel(bot.config['login_error_channel'])
    for cog, error in errors:
        print(error)
        await channel.send(f"**Error loading {cog}:**```{error}```")


if __name__ == '__main__':
    for cog in initial_extensions:
        try:
            bot.load_extension(f'cogs.{cog}')
            print(f'Loaded {cog}')
        except ExtensionError:
            errors.append([cog, str(traceback.format_exc())])
            print(f'Failed to load {cog}')

    checks.setup(bot)

    print('Logging in')
    bot.run()
