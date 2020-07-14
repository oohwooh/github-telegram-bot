from github import Github


def fork_repo(repoName, token):
    g = Github(token)
    github_user = g.get_user()
    repo = g.get_repo(repoName)
    myfork = github_user.create_fork(repo)
    return myfork