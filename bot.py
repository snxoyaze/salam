import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)




class pbot(Client):

    def __init__(self):
        super().__init__(
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"], 
            workers=50,
            plugins={"root": "luna_songbot"},
            sleep_threshold=5,
        )

        

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = pbot()
app.run()
