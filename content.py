from github import Github

#generated access token
access_token ="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"

login = Github(access_token)
user = login.get_user()
repo = user.get_repo("Testers")
contents = repo.get_contents("Hare.py")
print(contents)