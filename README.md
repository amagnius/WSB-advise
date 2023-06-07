# WSB-advise
Gathers and displays the current buy and sell recommendations from r/wallstreetbets

The website https://amagnius.github.io/WSB-advise/ sends a request to the backend to fetch the latest comments on the subreddit.
Sentiment analysis is performed on comments containing stock symbols in order to determine if the comment seems positive or negative.
This creates a score which is used to rank the top 3 stocks to buy and top 3 stocks to sell.
These are then displayed on the website. 
