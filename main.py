import os
import requests
from telethon import TelegramClient
from telethon.tl.types import Channel
from telethon.tl.types import MessageMediaDocument
from dotenv import load_dotenv
from datetime import datetime

from tqdm import tqdm

load_dotenv()

TOKEN = os.getenv("TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

TOKEN = TOKEN
# token can only be used for the bot, and since bot is not a member of the channel
# i want to download from, we can't use token.
# Remember to use your own values from `https://my.telegram.org/apps`!


client = TelegramClient('anon', int(API_ID), API_HASH)

CHANNEL_NAME = "🇳🇬AMUBIEYA ONLINE OFFICIAL CHANNEL©"


async def download_file(message, folder):
    # Create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    file_name = message.media.document.attributes[0].file_name
    # Download the document (file)
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path):
        # Check if the file sizes match
        local_size = os.path.getsize(file_path)
        remote_size = message.media.document.size
        if local_size == remote_size:
            print(f"File already exists: {file_name}")
            return
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=file_name) as t:
        await client.download_media(message, file=file_path, progress_callback=lambda current, total: t.update(current))
    print('File downloaded:', file_path)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # You can print all the dialogs/conversations that you are part of:
    # but in this case, i only need channels i belong to.
    async for dialog in client.iter_dialogs(limit=None):
        if isinstance(dialog.entity, Channel):
            pass

    entity = await client.get_entity(CHANNEL_NAME)
    # Iterate over all messages in the channel
    total = 0
    async for message in client.iter_messages(entity):
        try:
            if message.media and isinstance(message.media, MessageMediaDocument):
                total += 1
                file = message.media.document
                _id = file.id
                _name = file.attributes[0].file_name
                _date = message.date
                # print('File ID:', _id, "File name: ", _name, "Date uploaded: ", _date)
                await download_file(message, CHANNEL_NAME)
        except AttributeError:
            continue
    print("total discovered file is: ", total)


with client:
    client.loop.run_until_complete(main())
