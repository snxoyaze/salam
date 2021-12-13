from pyrogram import Client, filters
from youtube_search import YoutubeSearch
import requests

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


pbot = pyrogram.Client(
      "LUNA_SONGBOT",
       bot_token = os.environ["BOT_TOKEN"],
       api_id = int(os.environ["API_ID"]),
       api_hash = os.environ["API_HASH"],       
    )
pbot.run()
