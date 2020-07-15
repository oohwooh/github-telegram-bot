from github import Github


def listrepos():
    g = Github("GITHUB_TOKEN_HERE")
    for repo in g.get_user().get_repos():
        print(repo.name)
