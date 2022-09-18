import praw
import os
import logging

def init():
    global reddit
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_ID"),
                        client_secret=os.getenv("REDDIT_TOKEN"),
                        user_agent='buehlerclanbot by daveiator')
    logging.info("Reddit API online")


def subredditRand(sub):
    submission = reddit.subreddit(sub).random()
    return submission.url