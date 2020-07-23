from github import Github
import os

#take user token and name of repo

def watch_repo(GITHUB_TOKEN, repo_name): #call: g.getrepo(repo_name)
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    user = g.get_user() #login=NotSet by default
    #check if user starred repo already
    if user.has_in_watched(repo): #check if true
        user.remove_from_watched(repo)
        return "unwatched", repo.full_name
    else:
        user.add_to_watched(repo)
        return "watched", repo.full_name
