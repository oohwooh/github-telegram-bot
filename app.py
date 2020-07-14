from flask import Flask
from flask_github import Github

app = Flask(__name__)
app = config['GITHUB_CLIENT_ID'] = '2753a10ea2128ec4f9c8'
app = config['GITHUB_CLIENT_SECRET'] = 'b6f927c193e972551bfe7b8ef5ecc774f061c1db'

github = Github(app)

@app.route('/login')
def login():
    return github.authorize()

@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
    else:
        print (oauth_token)
        return "Authorized successfully!"

app.run(port="5000")pip
