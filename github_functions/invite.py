from github import Github

def invite_collab(repo_name, GITHUB_TOKEN, collaborator):
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo = g.get_repo(repo_name)
    addcollab = user.add_to_collaborators(collaborator, permission=admin)
    return addcollab