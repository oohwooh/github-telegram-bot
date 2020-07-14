from github import Github


def delete_repo(token = ""):
    g = Github(token)
    repo = g.get_repo("PyGithub/PyGithub")
    repo.delete()

delete_repo()