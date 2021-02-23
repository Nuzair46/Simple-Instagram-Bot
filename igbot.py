from instapy import InstaPy
import json

with open("config.json","r") as f:
	config = json.load(f)

username = config["username"]
password = config["password"]
api = config["api"]

tagfiles = open("hashtags.txt","r")
avoidfiles = open("avoidtags.txt","r")
commentfile = open("comments.txt","r")

tagCount = 0
hashtags = []

for line in tagfiles:
	hashtags.append(line)
	tagCount += 1
print(f"No. of hashtags = {tagCount}")

avoidCount = 0
avoidtags = []

for line in avoidfiles:
	avoidtags.append(line)
	avoidCount += 1
print(f"No. of Avoided hashtags = {avoidCount}")

commentCount = 0
comments = []

for line in commentfile:
	comments.append(line)
	commentCount += 1
print(f"No. of Comments = {commentCount}")

# Make changes Below

client = InstaPy(username=username, password=password, headless_browser=True, want_check_browser=False)
client.login()
client.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=20)
client.like_by_tags(hashtags, amount=10)
client.set_dont_like(avoidtags)

#uncomment to follow users.

#client.set_do_follow(True, percentage=20) 

#uncomment to comment on posts.

#client.set_do_comment(True, percentage=45) 
#client.set_comments(comments)

# use only if you use clarifai API
#client.set_use_clarifai(enabled=True, api_key=api)
#client.clarifai_check_img_for(['nsfw'])

#Set follower bounds
client.set_relationship_bounds(enabled=True, max_followers=2000)

client.end()
