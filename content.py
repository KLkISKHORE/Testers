from github import Github

#generated access token
access_token ="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"

all=[]
login = Github(access_token)
user = login.get_user()
repo = user.get_repo("Testers")
contents = repo.get_contents("Hari.txt")

print(contents.sha)