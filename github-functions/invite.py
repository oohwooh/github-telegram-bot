from github import Github

def invitecollab(repoName, token, collaborator)
g = Github(token)
github_user = g.get_user()
repo = g.get_repo(repoName)
addcollab = github_user.add_to_collaborators(collaborator, permission= admin)
return addcollab