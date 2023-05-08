import praw

reddit = praw.Reddit(
    client_id="ca67SLBHFy2Am7kPZ-TdKA",
    client_secret="m735OX5eD595ZhxYom1w5RssVyjUyg",
    user_agent="website:https://amagnius.github.io/WSB-advise/:v1 (by u/Dazzling-Pollution-6)",
)

def getComments(subreddit, numComments):
    # Create an instance of the subreddit
    subreddit = reddit.subreddit(subreddit)

    # Read in latest comments to a list
    recent_comments = subreddit.comments(limit=numComments)

    return recent_comments

