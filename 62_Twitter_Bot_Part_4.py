import tweepy
import datetime

auth = tweepy.OAuthHandler("g4p3RlBL66Bx3FXgxMtT11Oee", "tTnCAoh0c8dePF7UjDzyuBtrbVK4wjYOnyZba9WGWaENAYdjW1")
auth.set_access_token("1311299305991364610-g91HUY6dYu0PiW9wwepORdj0Z0zVCq", "g82De7KjelWHwvp4O5M3TVdmn0nRLLStB4PTPsNEPCxDD")

api = tweepy.API(auth)


def publictweet():
    if datetime.date.today().weekday() == 0:
        tweet_to_publish = "Hi everyone, today is Monday.  #Monday"
    if datetime.date.today().weekday() == 1:
        tweet_to_publish = "Enjoy your Tuesday.  #Tuesday"
    if datetime.date.today().weekday() == 2:
        tweet_to_publish = "Third day of the week.  # Wednesday"
    if datetime.date.today().weekday() == 3:
        tweet_to_publish = "Thursday! I can't wait for the weekend."
    if datetime.date.today().weekday() == 4:
        tweet_to_publish = "Friday... Finally"
    if datetime.date.today().weekday() == 5:
        tweet_to_publish = "Great! It is Saturday.  #weekend #Saturday"
    if datetime.date.today().weekday() == 6:
        tweet_to_publish = "Sunday Morning... #weekend #Enjoy"
    return tweet_to_publish


tweet = publictweet()
api.update_status(tweet)
print(tweet)
