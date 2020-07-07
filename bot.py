#Elizabeth is trying to use the tutorial

#some packages are built-in but for others you need to import // others req installing pip (pip install python-telegram-bot)
from telegram.ext import Updater
updater = Updater(token='TOKEN', use_context=True) #use_context=True is special for v12 of library; default=False
dispatcher = updater.dispatcher #introduce locally for updater quicker access to dispatcher

import logging #logging module setup to know when/why if things don't work
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

