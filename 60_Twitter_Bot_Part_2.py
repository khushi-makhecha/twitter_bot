import tweepy

auth = tweepy.OAuthHandler("XR7Bb9rSGitksk7iDnUzMqi5J", "yjCvQqxLj3wzSFPvDfm5LhGXoU4E9C7ZgibRwRDC97ePlZzIJT")
auth.set_access_token("1311299305991364610-cnbobpxpKhE5bYqfTPtiY361pn1HxA", "dgo2HNDDtvyY13WqiN2YbwCkjXpBNbkhdw1fHfR8z6liV")

api = tweepy.API(auth)
user2 = api.get_user("Cristiano")

for follower in user2.followers():
    print(follower.name)

# Because of Rate Limits, one can obtain only the specified number of names.

print(user2.followers_count)
