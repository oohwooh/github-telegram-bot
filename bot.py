#Elizabeth is trying to use the tutorial
#run: $Env:BOT_TOKEN = 'TOKEN_HERE'; python bot.py

import os
import github

#some packages are built-in but for others you need to import // others req installing pip (pip install python-telegram-bot)
from telegram.ext import Updater
from telegram.ext import PicklePersistence, CallbackQueryHandler #PicklePersistence: utility class, lets us save data about bot to a file
from github_functions import repo_overview, starrepo, watchrepo

persistence = PicklePersistence(filename='data')
updater = Updater(token=os.getenv("BOT_TOKEN"), persistence = persistence, use_context=True) #use_context=True is special for v12 of library; default=False
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
from telegram import InlineKeyboardMarkup


def repo_info(update, context):
    if "token" in context.user_data:
        desc, keyboard = repo_overview(context.args[0], context.user_data["token"])
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text=desc, reply_markup=reply_markup)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text="Not logged in. Please use the /auth command to log in.")


repo_info_handler = CommandHandler("repo", repo_info)
dispatcher.add_handler(repo_info_handler)
# use MessageHandler with command filter to reply to all unrecognized commands


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    # 'watch_xxxxx (repo id)'
    if query.data.startswith('star'):
        repo_id = int(query.data.replace('star_', '')) # repo_id = 'xxxxxxx'
        # User's auth token will be update.user_data['token']
        star_repo(update.user_data['token'], repo_id)
        
    if query.data.startswith('watch'):
        repo_id = int(query.data.replace('watch_', '')) # repo_id = 'xxxxxxx'
        # User's auth token will be update.user_data['token']
        watch_repo(update.user_data['token'], repo_id)
    
    # another way to do this is f"Selected option: {query.data}"
    query.edit_message_text(text="Selected option: {}".format(query.data))
    # selected option: watch_277662457

updater.dispatcher.add_handler(CallbackQueryHandler(button))


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

from github import Github

def auth(update, context):
    try:
        g = Github(context.args[0])
        user = g.get_user()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Logged in as" + user.name + "(" + user.login + ")" )
        context.user_data["token"] = context.args[0]
        #/auth will get set to user.context_data['token']

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid input. Enter token like '/auth token'")


auth_handler = CommandHandler("auth", auth )
dispatcher.add_handler(auth_handler)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


#added lastly: (if added it could be trigger before CommandHandlers has chance to update)
#to circumvent this, keyword argument group (int) can be passed to add_handler with a value other than 0
#updater.stop()
updater.idle()


# results = list()
# for repo in search_repos(query):
#     desc, keyboard = repo_overview()
#     results.append(InlineQueryResultArticle) (
#         id=repo.id,
#         title=repo.name,
#         input_message_content=desc
#         reply_markup=keyboard
#         url
#     ))