from github import Github


def search_repos(token = ""):
    g = Github(token)
    repos = g.search_repositories(query = "test", sort = 'updated', order = 'asc')
    print(repos)


search_repos()