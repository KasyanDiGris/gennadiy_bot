import config

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import *
import logging

def inline_request(bot, update):
    print("request")
    query = update.inline_query.query
    results = list()
    results.append(
            InlineQueryResultArticle(
                id="Pidor",
                title='Pidor',
                description="Sosnul",
                input_message_content=InputTextMessageContent("Ты пидор и сосал")
            )
    )
    results.append(
            InlineQueryResultArticle(
                id="go_drink",
                title='Go',
                description="Beer",
                input_message_content=InputTextMessageContent("Го бухать")
            )
    )
    print (results)
    bot.answer_inline_query(update.inline_query.id, results)

def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    updater = Updater(token=config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(inline_request))
    updater.start_polling()
