import config

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import *
import logging
import os
from yaml import load as yaml_load
import re
import random


inline_query_variants = []


def inline_request(bot, update):
    logging.debug("request")

    query = update.inline_query.query
    results = list()

    for node in inline_query_variants:
        item = {k: node[k] for k in ['id', 'title', 'description']}
        item['input_message_content'] = InputTextMessageContent(random.choice(node['variants']))

        results.append(InlineQueryResultArticle(**item))

    logging.debug(results)

    bot.answer_inline_query(update.inline_query.id, results, cache_time=1, is_personal=True)


def load_inline_query_variants():
    global inline_query_variants

    for node in os.listdir(config.INLINE_QUERY_VARIANTS_DIR):
        path = os.path.join(config.INLINE_QUERY_VARIANTS_DIR, node)

        if not os.path.isfile(path):
            continue

        data = yaml_load(open(path, 'r').read())
        data['id'] = re.sub(r'\W', '_', re.sub(r'\.yaml$', '', node)).lower()

        inline_query_variants.append(data)

    if len(inline_query_variants) == 0:
        raise Exception(random.choice([
            'Пошёл нахуй, уёбок!',
            'Мать твою ебал!',
            'Сосни-ка хуйца, мразь!',
        ]))


def start():
    random.seed()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    load_inline_query_variants()

    updater = Updater(token=config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(inline_request))
    updater.start_polling()
