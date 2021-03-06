# CTBOT
[![Discord](https://img.shields.io/discord/672129232146661377)](https://discord.gg/vJGBSnW)

![language](https://img.shields.io/badge/language-python-blue)
![python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Welcome to CTBot, the official bot of the Followers of the Crafting Table.

Feel free to open a pull request and add anything you like! Join the dev discord to be added as an instant-push contributor.

## Getting Started

You'll need Python 3.6 or higher to run the bot due to f-strings and dependencies.

### Installation
1. Clone this repository.
```
git clone https://github.com/FrequencyX4/CTBot
```
2. Install the dependencies.
```py
pip install -r requirements.txt
```
### Running
```py
python bot.py
```

> Make sure you are using the appropriate version of Python! If the `python` command runs Python 2 on your OS, you should use `python3` and `pip3` instead.
>
> If you're experiencing a `CERTIFICATE_VERIFY_FAILED` error on macOS, you will have to [install certificates](https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore).

## License
This project is licensed under the GNU Lesser General Public License (except for pyMine, TODO move to another repo). Check [LICENSE](https://github.com/FrequencyX4/CTBot/blob/master/LICENSE) for more details.


## Contributors
- @FrequencyX4 (Luck#1574)
- @borisnliscool (Boris NL#3982)
- @ProgrammerPlays (ProgrammerPlays#8264)
- @Lach993 (Lach993#4250)
- @korochun (korochun#3452)
- @legendary-galfar (galfar#9119)
- @mouncg (EPFFORCE#1337)
- @MinerChAI (Mr_ChAI#1824)


## What are the Followers of the Crafting Table?
The Followers of the Crafting Table are a semi-religious group created on 2b2t in January 2020. We make builds with/of crafting tables like the Crafting Table Valley or the super-sized crafting tables that are now common close to spawn. 

## How can I set up a development mirror?
Setting up a development mirror greatly helps us in case our main VPS goes down, and also allows us to test new features.
1. Join the Discord.

At the top of this file there is a link to join the dev Discord (the "chat" shield). You must join it to have your mirror recognized.

2. Install and run 24/7.

Following the installation instructions, run the bot and keep it up 24/7. You can just leave a computer, RPi, or Arduino on long-term to do this.

3. Ask the devs to recognize the mirror.

On approval of your mirror, the devs will add it to the development Discord for testing.
