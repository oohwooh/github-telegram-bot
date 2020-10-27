from flask import Flask
from flask_github import GitHub
import os

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = os.getEnv('GITHUB_CLIENT_ID') # 'CLIENT_ID_HERE'
app.config['GITHUB_CLIENT_SECRET'] = os.getEnv('GITHUB_CLIENT_SECRET') # 'CLIENT_SECRET_HERE'

github = GitHub(app)

# @app.test('/')
# def index():
#     return "HELLO WORLD!!!!!!!!!!!!!!!!!!!!!!!"
# app.run(host="0.0.0.0", port="7000")

@app.route('/auth/<int:user_id>') # route in app that has parameter for user_id; stores in session
def route(user_id):
    return github.authorize()

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


app.run(port="5000") # port 80=http; port 443=https
