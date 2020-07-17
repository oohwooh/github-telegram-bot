from github import Github
import os

def delete_repo(GITHUB_TOKEN, repo_name): #x="" is an optional parameter (if no input, it's default)
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    repo.delete()

delete_repo(os.getenv('GITHUB_TOKEN'), "elizabethqiu/testcreaterepo") #here you need to specify under users