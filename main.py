import os

import praw
import pymongo

import helper

# Client setup
mongoDBClient = pymongo.MongoClient(os.environ.get("MONGO_DB_STRING"))
db = mongoDBClient["bot"]

client = praw.Reddit(client_id=os.environ.get("CLIENT_ID"),
                    client_secret=os.environ.get("CLIENT_SECRET"),
                    password=os.environ.get("PASSWORD"),
                    username=os.environ.get("USERNAME"),
                    user_agent=os.environ.get("USER_AGENT"))

subreddit = client.subreddit(os.environ.get("SUBREDDIT"))

# Working logic
for activity in subreddit.mod.stream.log(action='editflair', skip_existing=True):
    
    try:
        post_url = "https://www.reddit.com" + activity.target_permalink
        post = client.submission(url = post_url)

        # Check if post needs to be removed (match flair)
        if post.link_flair_template_id in helper.removal:

            # Check if already commented
            duplicate = db.bot.find_one({"post_id":post.id})            

            if duplicate: # Delete the previous comment and it's DB entry
                comment = client.comment(duplicate['comment_id'])
                comment.delete()
                db.bot.delete_one({'_id': duplicate['_id']})

            # Post a sticky citing the rule that caused the removal
            sticky = post.reply(helper.removal_sticky(helper.removal[post.link_flair_template_id]))
            sticky.mod.distinguish(how='yes', sticky=True)

            post.mod.remove()

            removal_log = {
                "post_id":post.id,
                "post_url":post.url,
                "comment_id":sticky.id,
                "post_submission_date":post.created_utc,
                "flair":post.link_flair_template_id
            }
            db.bot.insert_one(removal_log) # Record the post and comment

            print("Post removed: "+activity.target_permalink)
        else:
            # Post won't be removed, check is there's a sticky
            duplicate = db.bot.find_one({"post_id":post.id})

            if duplicate: # If found remove it and the DB entry
                print("dupe found")
                comment = client.comment(duplicate['comment_id'])
                comment.delete()
                db.bot.delete_one({'_id': duplicate['_id']})
            print("Comment deleted")
    except Exception as e:
        print('Error: '+ str(e))
    
