from flask import Flask
from flask_github import GitHub

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = 'CLIENT_ID_HERE'
app.config['GITHUB_CLIENT_SECRET'] = 'CLIENT_SECRET_HERE'

github = GitHub(app)


@app.route('/login')
def login():
    return github.authorize()


@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        return "Authorization failed."
    else:
        print(oauth_token)
        return "Authorized successfully!"


app.run(port="5000")
