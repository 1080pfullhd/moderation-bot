
import os
# List of template-IDs and their removal reason
removal = {
    '8aabcc16-ac62-11ea-86b2-0e1c41d7e1eb':'R1: "Follow the Redditquette"',
    'cf9999e8-ac62-11ea-aa9c-0ee0adec2b9f':'R2: "Do not harass, attack, or insult other users."',
    'e217b1d2-17b3-11ec-b085-ee31f54aaf15':'R4: "No pronography or death"',
    '95811a06-1172-11e9-bfa4-0e39c69bf0b6':'R5: "No recent reposts from this subreddit"',
    '1aea7d22-ac63-11ea-83c8-0e7f5dcefe35':'R6: "All posts must show a *living thing* attempting something in *real life*"',
    'b6f4072a-1172-11e9-a760-0ed5d0fbfc06':'R7: "All posts must show an *unsuccessful* attempt"',
    'a4ee3bfe-1172-11e9-a721-0e7b2cd76162':'R7: "All posts must show an *unsuccessful* attempt"',
    '8c4dd04a-ac63-11ea-bc72-0e8e1bd13beb':'R8: "No low effort posts, screenshots or links to third-party sites"',
    'f9220eba-f5c0-11ea-b1c8-0e856f675065':'R9: "Staged attempts are not allowed',
}

# Comment generator
def removal_sticky(reason):
    comment = f'''Thank you for your submission to r/{str(os.environ.get("SUBREDDIT")).strip("r/")}. Unfortunately, your post was removed for violating the following rule:

> {reason}

If you have any questions regarding this removal, please contact the moderators of this subreddit by sending a modmail. [Click this link to send a modmail](https://www.reddit.com/message/compose/?to=r/{str(os.environ.get("SUBREDDIT")).strip("r/")}).

^(This is a bot account, direct messages and chat requests go to an unmonitored inbox)'''

    return comment

