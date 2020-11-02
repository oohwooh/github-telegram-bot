from github import Github

def fork_repo(repo_name, GITHUB_TOKEN):
    g = Github(GITHUB_TOKEN)
    github_user = g.get_user()
    repo = g.get_repo(repo_name)
    myfork = github_user.create_fork(repo)
    return myfork