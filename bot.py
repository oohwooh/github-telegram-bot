#Elizabeth is trying to use the tutorial

#some packages are built-in but for others you need to import // others req installing pip (pip install python-telegram-bot)
from telegram.ext import Updater
import os
updater = Updater(token=os.getenv("BOT_TOKEN"), use_context=True) #use_context=True is special for v12 of library; default=False
dispatcher = updater.dispatcher #introduce locally for updater quicker access to dispatcher

import logging #logging module setup to know when/why if things don't work
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

