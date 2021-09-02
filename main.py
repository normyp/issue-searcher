from github import Github
import os
import time

# First create a Github instance:
access_token = os.environ['ACCESS_TOKEN']
# using an access token

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", login_or_token=access_token, per_page=100)

i = 0
# Then play with your Github objects:
for issue in g.search_issues('', sort="created", order="desc", label="good-first-issue"):
    print(issue)
    print(issue.url)
    i += 1
    print(i)

