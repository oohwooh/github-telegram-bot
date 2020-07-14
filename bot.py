#Elizabeth is trying to use the tutorial
#run: $Env:BOT_TOKEN = 'TOKEN_HERE'; python bot.py

#some packages are built-in but for others you need to import // others req installing pip (pip install python-telegram-bot)
from telegram.ext import Updater
import os
updater = Updater(token=os.getenv("BOT_TOKEN"), use_context=True) #use_context=True is special for v12 of library; default=False
dispatcher = updater.dispatcher #introduce locally for updater quicker access to dispatcher

import logging #logging module setup to know when/why if things don't work
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#/start command calls this: returns welcome message
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello and welcome. I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

#listens for regular messages and echoes them; MessageHandler class and Handler subclass
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

#/caps command calls this; takes text and replies in caps
#can receive the arguments (as a list, split on spaces) passed to command in callback function
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

#/setinline command calls this; bot call on command via inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

#use MessageHandler with command filter to reply to all unrecognized commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#added lastly: (if added it could be trigger before CommandHandlers has chance to update)
#to circumvent this, keyword argument group (int) can be passed to add_handler with a value other than 0
#updater.stop()