from github import Github


def repo_overview(token = ""):
    g = Github(token)
    repo = g.get_repo("PyGithub/PyGithub")
    print("This repo is written in " + repo.get_languages() + " and the description for the repo is: " + 
    repo.description)

repo_overview()