from github import Github

def search_repos(GITHUB_TOKEN, query):
    g = Github(GITHUB_TOKEN)
    repos = g.search_repositories(query=query, sort='updated', order='asc')
    print(repos)

#search_repos()