import os
from os import environ
import logging
from config import BOT_TOKEN, API_ID, API_HASH 

#  logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")
LOG = logging.getLogger(__name__)



class pbot: bot_token = BOT_TOKEN
            api_id = API_ID
            api_hash = API_HASH
            workers=50,
            plugins={"root": "LUNA_SONGBOT"},
            sleep_threshold=5,
        )

        

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = pbot()
app.run()
