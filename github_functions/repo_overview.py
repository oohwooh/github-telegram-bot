from github import Github
from telegram import InlineKeyboardButton

def repo_overview(repoName, token):
    g = Github(token)
    repo = g.get_repo(repoName)
    desc = "This repo is written in " + str(repo.get_languages()) + " and the description for the repo is: " + repo.description
    keyboard = [[InlineKeyboardButton("⭐", callback_data='star_'+str(repo.id)), InlineKeyboardButton("👀", callback_data='watch_'+str(repo.id))], [InlineKeyboardButton("Open in GitHub", url=repo.url)]]
    return desc, keyboard
