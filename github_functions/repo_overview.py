from github import Github
from telegram import InlineKeyboardButton

def repo_overview(repoName, token):
    g = Github(token)
    repo = g.get_repo(repoName)
    desc = "Description: " + repo.description + "\n Languages: " + str(repo.get_languages()) + "\n Watchers: " + str(repo.watchers_count) + " \n Stargazers: " + str(repo.stargazers_count) + " \n Forks: " + str(repo.forks_count)
    keyboard = [[InlineKeyboardButton("⭐", callback_data='star_'+str(repo.id)), InlineKeyboardButton("👀", callback_data='watch_'+str(repo.id))], [InlineKeyboardButton("Open in GitHub", url=repo.url)]]
    return desc, keyboard
