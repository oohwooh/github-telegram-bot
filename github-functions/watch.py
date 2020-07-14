from github import Github

def watch(repoName, token, watched)
g = Github(token)
github_user = g.get_user()
repo = g.get_repo(repoName)
watch = github_user.add_to_watched(watched)
return watch

