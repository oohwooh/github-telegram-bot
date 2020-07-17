from github import Github

def watch(repo_name, GITHUB_TOKEN, watched)
g = Github(GITHUB_TOKEN)
user = g.get_user()
repo = g.get_repo(repo_name)
watch = user.add_to_watched(watched)
return watch

