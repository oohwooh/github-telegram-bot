from github import Github
import os

def create_repo(GITHUB_TOKEN, repo_name):
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    user.create_repo(repo_name)

#create_repo(os.getenv('GITHUB_TOKEN'), "testcreaterepo") #creating under user from GITHUB_TOKEN; no specification needed