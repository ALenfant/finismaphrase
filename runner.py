#!/usr/bin/env python

import tweepy
import logging
from config import create_api
import time
import os
import re

from sentence_completer import SentenceCompleter

BOT_NAME = "FinisMaPhrase"
TWEET_LENGTH = 280

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "last_id.txt")
sentence_completer = SentenceCompleter()
pattern = re.compile("@%s" % BOT_NAME, re.IGNORECASE)


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        logger.info(f"Answering to {tweet.user.name}")

        if not tweet.user.following:
            tweet.user.follow()

        text = tweet.text
        text = pattern.sub("", text).strip()  # Remove the bot's name
        logger.info(f"Sentence prefix:{text}")
        completed_sentence = sentence_completer.complete_prettify_shorten_sentence(text, length=TWEET_LENGTH)

        api.update_status(
            status=completed_sentence,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True,
        )
    return new_since_id


def read_last_id():
    try:
        with open(path, "r") as f:
            last_id = int(f.readline())
    except (FileNotFoundError, ValueError):
        last_id = 1
    return last_id


def write_last_id(last_id):
    with open(path, "w") as f:
        f.write(str(last_id))


if __name__ == "__main__":
    logger.info("Initializing bot runner")
    api = create_api()
    since_id = read_last_id()
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        write_last_id(since_id)
        logger.info("Waiting...")
        time.sleep(60)

