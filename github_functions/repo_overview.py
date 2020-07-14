from github import Github
from telegram import InlineKeyboardButton

def repo_overview(repoName, token):
    g = Github(token)
    repo = g.get_repo(repoName)
    desc = "This repo is written in " + repo.get_languages() + " and the description for the repo is: " + repo.description
    keyboard = [[InlineKeyboardButton("⭐", callback_data='star_'+repo.id), InlineKeyboardButton("👀", callback_data='watch_'+repo.id)], [InlineKeyboardButton("Open in GitHub", url=repo.url)]]
    return desc, keyboard
