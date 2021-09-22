import tweepy

auth = tweepy.OAuthHandler("XR7Bb9rSGitksk7iDnUzMqi5J", "yjCvQqxLj3wzSFPvDfm5LhGXoU4E9C7ZgibRwRDC97ePlZzIJT")
auth.set_access_token("1311299305991364610-cnbobpxpKhE5bYqfTPtiY361pn1HxA", "dgo2HNDDtvyY13WqiN2YbwCkjXpBNbkhdw1fHfR8z6liV")

api = tweepy.API(auth)
user = api.me()

print(user.screen_name)
print(user.followers_count)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print(tweepy.Cursor(api.followers))
print(tweepy.Cursor(api.followers).items())
print(list(tweepy.Cursor(api.followers).items()))

# for follower in tweepy.Cursor(user.followers).items():                    # Doing this will give an error.
for follower in tweepy.Cursor(api.followers).items():

    if follower.name == "Something":
        follower.follow()
        print("Followed", follower.name)

    print(follower.name)

