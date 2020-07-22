from github import Github
import os

def recent_commits(GITHUB_TOKEN, repo_name, n):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name) # user input
    for commit in repo.get_commits()[:n]: # view n most recent commits
        print (commit.author, commit.commit.message)

# recent_commits(os.getenv('GITHUB_TOKEN'), "oohwooh/github-telegram-bot") # need to interact with paginated list afterwards