import os
from os import environ
from pyrogram import Client, filters
import logging
from config import Config
import pyrogram


#  logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")
LOG = logging.getLogger(__name__)



pbot = pyrogram.Client(
      "luna_songbot",
       bot_token=Config.BOT_TOKEN,
       api_id=Config.APP_ID,
       api_hash=Config.API_HASH,
       plugins={"root": "LUNA_SONGBOT"},
       sleep_threshold=5,
   )

        



app = pbot()
app.run()
