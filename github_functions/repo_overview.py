from github import Github
from telegram import InlineKeyboardButton
from github import Repository

def repo_overview(repo_name, GITHUB_TOKEN):
    if type(repo_name) == str:
        g = Github(GITHUB_TOKEN)
        try:
            repo = g.get_repo(repo_name)
        except:
            return "repo name does not exist", None # Null object in Python
    elif type(repo_name) == Repository:
        repo = repo_name
    if (repo.description): # Python will convert this: it means "if this repo description exists (true)"
        desc = "Description: " + repo.description
    else:
        desc = ""
    desc = desc + "\n Languages: " + str(repo.get_languages()) + "\n Watchers: " + str(repo.watchers_count) + " \n Stargazers: " + str(repo.stargazers_count) + " \n Forks: " + str(repo.forks_count)
    keyboard = [[InlineKeyboardButton("⭐", callback_data='star_'+str(repo.id)), InlineKeyboardButton("👀", callback_data='watch_'+str(repo.id))], [InlineKeyboardButton("Open in GitHub", url=repo.url)]]
    return desc, keyboard # desc in String, keyboard is nested list