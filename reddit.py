import praw
import utils

reddit = praw.Reddit(client_id=utils.getAttribute('reddit_id'),
                    client_secret= utils.getAttribute('reddit_token'),
                    user_agent='buehlerclanbot by daveiator')
print("Reddit API online")


def subredditRand(sub):
    submission = reddit.subreddit(sub).random()
    return submission.url