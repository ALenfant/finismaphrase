# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    # Ensure we have all the necessary info
    for env_key in ("TWITTER_API_KEY", "TWITTER_SECRET_KEY", "TWITTER_BOT_ACCESS_KEY", "TWITTER_BOT_ACCESS_SECRET"):
        if env_key not in os.environ:
            raise Exception("Missing environment key %s" % env_key)

    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_SECRET_KEY")
    access_token = os.getenv("TWITTER_BOT_ACCESS_KEY")
    access_token_secret = os.getenv("TWITTER_BOT_ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
