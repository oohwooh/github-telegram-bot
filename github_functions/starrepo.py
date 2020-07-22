from github import Github
import os

# take user token and name of repo

def star_repo(GITHUB_TOKEN, repo_name):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name) # call: get_repo('oohwooh/github-telegram-bot') OR get_repo(xxxxxxx)
    user = g.get_user() # login=NotSet by default
    # check if user starred repo already
    if user.has_in_starred(repo): # check if true
        user.remove_from_starred(repo)
    else:
        user.add_to_starred(repo)