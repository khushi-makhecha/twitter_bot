import tweepy

auth = tweepy.OAuthHandler("XR7Bb9rSGitksk7iDnUzMqi5J", "yjCvQqxLj3wzSFPvDfm5LhGXoU4E9C7ZgibRwRDC97ePlZzIJT")
auth.set_access_token("1311299305991364610-cnbobpxpKhE5bYqfTPtiY361pn1HxA", "dgo2HNDDtvyY13WqiN2YbwCkjXpBNbkhdw1fHfR8z6liV")

api = tweepy.API(auth)

search_str = "Python"
number_of_tweets = 10

for tweet in tweepy.Cursor(api.search, search_str).items(number_of_tweets):
    print(tweet)
    print(tweet.text)