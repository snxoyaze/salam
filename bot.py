import os
from os import environ
from pyrogram import Client, filters
import logging
import pyrogram


#config
BOT_TOKEN = environ['BOT_TOKEN']
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']



#  logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")
LOG = logging.getLogger(__name__)



pbot = pyrogram.Client(
      "luna_songbot",
       bot_token=BOT_TOKEN,
       api_id=APP_ID,
       api_hash=API_HASH,
       plugins={"root": "LUNA_SONGBOT"},
       sleep_threshold=5,
   )

        



app = pbot()
app.run()
