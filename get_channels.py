import os
from telethon import TelegramClient
from dotenv import load_dotenv
from telethon.tl.types import Channel, User, Chat, MessageMediaDocument, PeerChannel

load_dotenv()


# Remember to use your own values from my.telegram.org!
TOKEN = os.getenv("TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
client = TelegramClient('anon', int(API_ID), API_HASH)


async def get_channels():
    """
    This function would print out all the channels you currently
    are a member of.

    `isinstance(dialog.entity, Channel)` check to see if the instance is a Channel instance (group).
    """
    async for dialog in client.iter_dialogs(limit=None):
        if isinstance(dialog.entity, Channel):
            print('Channel ', dialog.name, 'has ID', dialog.id, ' and title is: ', dialog.title)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # You can print all the dialogs/conversations that you are part of:
    print("You are subscribed to following channels:")
    await get_channels()



with client:
    client.loop.run_until_complete(main())

"""
You are subscribed to following channels:
Channel  Shaykh Dr. Luqman Idris Sekoni Lectures has ID -1001427967564
Channel  At-Tasfiyah wat-Tarbiya has ID -1001436110603
Channel  Dr. Sharafuddeen Raji Lectures has ID -1001349165996
Channel  Skill Afrika has ID -1001244927737
Channel  LAUMGA National/International Forum has ID -1001484431084
Channel  Web Design Class has ID -1002002003660
Channel  Learn Web Development has ID -1001894723266
Channel  🇳🇬AMUBIEYA ONLINE OFFICIAL CHANNEL© has ID -1001379455070


"""
