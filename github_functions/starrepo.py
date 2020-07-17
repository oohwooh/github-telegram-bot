from github import Github

#take user token and name of repo

def star_repo(GITHUB_TOKEN, repo_name): #call: g.getrepo(repo_name)
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    user = g.get_user() #login=NotSet by default
    #check if user starred repo already
    if user.has_in_starred(repo): #check if true
        user.remove_from_starred(repo)
    else:
        user.add_to_starred(repo)
