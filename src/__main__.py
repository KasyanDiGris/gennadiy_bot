import bot
import os
import config

if __name__ == "__main__":
    config.BOT_TOKEN = os.environ["GENNADIY_BOT_TOKEN"]
    bot.start()
