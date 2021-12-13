import logging

#  logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")
LOG = logging.getLogger(__name__)



class pbot:

    def __init__(self):
        super().__init__(
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"], 
            workers=50,
            plugins={"root": "LUNA_SONGBOT"},
            sleep_threshold=5,
        )

        

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = pbot()
app.run()
