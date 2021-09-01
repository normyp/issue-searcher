from github import Github
import os

# First create a Github instance:
access_token = os.environ['ACCESS_TOKEN']
# using an access token
g = Github(access_token)

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", login_or_token=access_token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)