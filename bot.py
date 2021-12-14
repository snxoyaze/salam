import os
from os import environ
import logging

#  logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")
LOG = logging.getLogger(__name__)



class pbot: api_id = int(environ['API_ID'])
            api_hash = environ['API_HASH']
            bot_token = environ['BOT_TOKEN']
            workers=50,
            plugins={"root": "LUNA_SONGBOT"},
            sleep_threshold=5,
        )

        

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = pbot()
app.run()
