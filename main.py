import requests
from github import Github
import os
import json
import time

# First create a Github instance:
access_token = os.environ['ACCESS_TOKEN']
# using an access token

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", login_or_token=access_token, per_page=100)

i = 0
f = open("issues.txt", "w").close()



# Then play with your Github objects:
for issue in g.search_issues('', sort="created", order="desc", label="good-first-issue"):
    if "bot" in issue.user.login:
        print(issue)
        print(issue.url)
        i += 1
        print(i)
        print("this is a bot issue")
        print(issue.user.login)
        #time.sleep(2.0)
    else:
        print(issue)
        print(issue.url)
        repoLang = requests.get(issue.repository.url + "/languages")
        lang = json.loads(repoLang.text)
        print(lang)
        if "Python" in lang:
            if lang["Python"] > 450000:
                f = open("issues.txt", "a")
                # f.write(issue.)
                f.write(issue.html_url)
                f.write("\n")
                f.close()
                print("Is python")
        save = True
        i += 1
        print(i)

