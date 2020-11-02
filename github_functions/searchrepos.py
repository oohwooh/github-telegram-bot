from github import Github
from telegram import InlineQuery
from .repo_overview import repo_overview

def search_repos(GITHUB_TOKEN, query):
    g = Github(GITHUB_TOKEN)
    if query == "":
        return("*add some default text here*")
    repos = g.search_repositories(query, order='asc')
    return(repos)


from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'Caps',
            input_message_content = InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)