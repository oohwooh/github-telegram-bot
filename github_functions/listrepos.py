from github import Github

def list_repos():
    g = Github("GITHUB_TOKEN_HERE")
    for repo in g.get_user().get_repos():
        print(repo.name)
