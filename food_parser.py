import twitter
import time
import itertools

class MurielTwitterFeed:
    
    _twitter_api = None

    def __init__(self, 
        twitter_consumer_key, twitter_consumer_secret,
        twitter_access_token_key, twitter_access_token_secret):
        self._twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret,
                                        access_token_key=twitter_access_token_key, access_token_secret=twitter_access_token_secret,
                                        tweet_mode="extended")
    
    def today_menu(self):
        muriel_tweets = self._twitter_api.GetUserTimeline(screen_name="bar_muriel", exclude_replies=True, count=20)
        today_menu_tweets = list(filter(self._tweet_was_created_today, muriel_tweets))
        today_menu = list()
        for tweet in today_menu_tweets:
            for tweet_line in tweet.full_text.splitlines():
                if self._is_food(tweet_line):
                    today_menu.append(tweet_line)

        return today_menu
    
    def _is_food(self, menu_entry):
        return not len(menu_entry) == 0 and \
            not "Menú del día" == menu_entry and \
            not "CARNES" == menu_entry and \
            not "PESCADOS" == menu_entry and \
            not "POSTRES" == menu_entry

    def _tweet_was_created_today(self, tweet):
        tweet_date = time.localtime(tweet.created_at_in_seconds)
        today_date = time.localtime()
        return today_date.tm_yday == tweet_date.tm_yday
