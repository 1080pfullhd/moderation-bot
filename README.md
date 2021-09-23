# Subreddit moderation bot
This bot will remove posts by matching their flairs with the templates listed in `helper.py`

## Features
- Removes post whose post-flair template matches the configured templates
- Comments a sticky citing the reason for the removal
- Changes the comment if flair is changed (old comment is deleted and a new is posted, this will send another comment notification to OP)
- Deletes the comment if flair isn't listed for removal or post has no flair

## Database choice
To prevent being rate limited, the bot maintains an internal database of posts on which the bot posted a stickied comment.
I went with  MongoDB as it's managed variant MongoDB Atlas has a really generous free tier. Their `M0-Sandbox` should be able to handle a couple years'
worth of records before needing a cleanup. 

## Installation help
If you require any help with deploying it or need some help in tweaking it, just open an issue. 

## Installation

#### Dependencies
If you use `pipenv` then install the dependencies with 
```
pipenv install
```
This requires `python 3.6` but you can manage without it if you're within a virtual environment.

Alternatively the two required dependencies can be installed with
```
pip install praw pymongo[srv]
```
#### App setup
Then export the following environment variables (the client-id and secret should be of script-application type):
1. `CLIENT_ID` : 14 character Reddit app client ID 
1. `CLIENT_SECRET` : 27 character Reddit app client secret
1. `USERNAME` : Username of the reddit account (should be a moderator on the subreddit)
1. `PASSWORD` : Account password
1. `USER_AGENT` : User-Agent string
1. `SUBREDDIT` : Subreddit that will be moderated
1. `MONGO_DB_STRING` : The connection string that'll connect to the MongoDB instance

Instead of exporting them as environment variables these can be hard-coded into the code. For doing that, replace `os.environ.get("xxx")`
with the corresponding variable.

#### Setting the flairs
- In the mod tools, go to post flairs and copy the template-ID of the flairs that will mark the post for removal.
- Paste them as the keys in the python-dict named `removal` inside `helper.py`. 
- The dict-values for those keys will be the removal message. This message will change for different flairs, the common part
is in the function `removal_sticky()` within `helper.py`

Once this setup is complete, the bot is ready to use. Start it with 
```
python main.py
```
For running it indefinitely, use `nohup` to detach and run the process in background
```
nohup python main.py
```
(If running with nohup, remember to kill multiple instances of the process otherwise the bot may behave unexpectedly)
### Deploy on Heroku
For deploying on heroku, set the aformentioned environment variable as the config vars. The Procfile in the project is ready for use.
Push the code on heroku and start the worker process.
