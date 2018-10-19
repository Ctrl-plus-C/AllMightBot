import tweepy
from jokes import random_joke
from quote import quote_generator


def tweett(c_list):
    consumer_key = "key_place_holder"
    consumer_secret = "key_place_holder"
    access_token = "key_place_holder"
    access_token_secret = "key_place_holder"
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    # import pdb; pdb.set_trace()
    api = tweepy.API(auth)
    # print(api.status_code)

    key = c_list[1]
    status = 0

    if key == 'joke':
        while True:
            joke_gen = random_joke()
            if len(joke_gen)<=139:
                break
        api.update_status(status=joke_gen)
        status = 1
    elif key == 'quote':
        while True:
            quote_gen = quote_generator()
            if len(quote_gen)<=139:
                break
        api.update_status(status=quote_gen)
        status = 2
    elif key == 'this':
        stts = ' '.join(c_list[2:])
        if len(stts)>139:
            status = -1
        else:
            api.update_status(status=stts)
            status = 3
    
    if status == -1:
        return "Character limit exceeded."
    elif status == 0:
        return "Wrong Usage\nFollow: tweet <joke|quote> or tweet <this> 'your tweet here' "
    elif status == 1:
        return "Tweeted joke"
    elif status == 2:
        return "Tweeted quote"
    elif status == 3:
        return "Tweeted"

