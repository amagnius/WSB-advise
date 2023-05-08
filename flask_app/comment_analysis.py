import praw

reddit = praw.Reddit(
    client_id="ca67SLBHFy2Am7kPZ-TdKA",
    client_secret="m735OX5eD595ZhxYom1w5RssVyjUyg",
    user_agent="website:https://amagnius.github.io/WSB-advise/:v1 (by u/Dazzling-Pollution-6)",
)

def readTickersToDictKeys(filename):
    # Initialize an empty dictionary
    stockRatings = {}

    # Read the text file line by line
    with open(filename, 'r') as file:
        for line in file:
            # Remove newline character and leading/trailing spaces from the line
            key = line.strip()

            # Add the key to the dictionary with a value of 0
            stockRatings[key] = 0
    
    return stockRatings

def getComments(subreddit, numComments):
    # Create an instance of the subreddit
    subreddit = reddit.subreddit(subreddit)

    # Read in latest comments to a list
    recent_comments = subreddit.comments(limit=numComments)

    return recent_comments

def analyzeComments(commentList):

