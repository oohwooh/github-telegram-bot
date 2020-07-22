from github import Github
from telegram import InlineQuery

def search_repos(GITHUB_TOKEN, query):
    g = Github(GITHUB_TOKEN)
    query = update.inline_query.query
    if query == "":
        return("*add some default text here*")
    repos = g.search_repositories(query, sort='updated', order='asc')
    context.bot.answer_inline_query(update.inline_query.id, repos)
    return(repos)

#search_repos()



