"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**Nessun nome setato.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("Userbot ✅ONLINE\n\n"
                     "`Versione Telethon: 6.9.0\nPython: 3.7.3\n Versione JK🦄: 0.3.beta\n`"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "`Userbot creato da:` [SnapDragon](tg://user?id=719877937), @anubisxx\n"
                     "`Tradotto da:` @xXjk6Xx, @ImSoJoker
                     f"`Userbot di:` {DEFAULTUSER}\n\n"
                     
