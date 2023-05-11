import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit = praw.Reddit(
    client_id="ca67SLBHFy2Am7kPZ-TdKA",
    client_secret="m735OX5eD595ZhxYom1w5RssVyjUyg",
    user_agent="website:https://amagnius.github.io/WSB-advise/:v1 (by u/Dazzling-Pollution-6)",
)

def read_tickers_to_dict_keys(filename):
    # Initialize an empty dictionary
    stock_tickers = {}

    # Read the text file line by line
    with open(filename, 'r') as file:
        for line in file:
            # Remove newline character and leading/trailing spaces from the line
            key = line.strip()

            # Add the key to the dictionary with a value of 0
            stock_tickers[key] = 0
    
    return stock_tickers

# Initialize dictionary contain all stock tickers as a global variable
stock_tickers = read_tickers_to_dict_keys("tickers.txt")

# Create an instance of a sentiment analyzer as a global variable
analyzer = SentimentIntensityAnalyzer()

def get_comments(subreddit, num_comments):
    # Create an instance of the subreddit
    subreddit = reddit.subreddit(subreddit)

    # Read in latest comments to a list
    recent_comments = subreddit.comments(limit=num_comments)

    return recent_comments

def analyze_comments(comment_list):

    stock_ratings = {}

    # Iterate through comments
    for comment in comment_list:
        words = comment.body.upper().split()
        for word in words:
            if word in stock_tickers:
                # Perform Sentiment analysis
                sentiment_score = analyzer.polarity_scores(comment.body)['compound']
                num_upvotes = comment.score
                total_score = sentiment_score * (1 + num_upvotes)
                if total_score != 0:
                    if word in stock_ratings:
                        stock_ratings[word] += total_score
                    else:
                        stock_ratings[word] = total_score
                # Go to the next comment   
                break
    
    # Sort the dictionary by values and store the result as a list of tuples
    sorted_by_values = sorted(stock_ratings.items(), key=lambda item: item[1])

    return sorted_by_values


def fetch_stock_recommendations():
    comment_list = get_comments("wallstreetbets", 1000)
    sorted_by_values = analyze_comments(comment_list)

    top_3_buy = []
    # Iterate through the last 3 elements in reversed order
    for element in sorted_by_values[-1:-4:-1]:
        if element[1] > 0:
            top_3_buy.append(element)

    top_3_sell = []

    for element in sorted_by_values[:3]:
        if element[1] < 0:
            top_3_sell.append(element)


    recommendations = [
        {'ticker': stock[0], 'action': 'buy'} for stock in top_3_buy
    ] + [
        {'ticker': stock[0], 'action': 'sell'} for stock in top_3_sell
    ]

    return recommendations
