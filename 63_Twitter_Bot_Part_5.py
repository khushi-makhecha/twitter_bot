import tweepy

auth = tweepy.OAuthHandler("g4p3RlBL66Bx3FXgxMtT11Oee", "tTnCAoh0c8dePF7UjDzyuBtrbVK4wjYOnyZba9WGWaENAYdjW1")
auth.set_access_token("1311299305991364610-g91HUY6dYu0PiW9wwepORdj0Z0zVCq", "g82De7KjelWHwvp4O5M3TVdmn0nRLLStB4PTPsNEPCxDD")

api = tweepy.API(auth)

# api.create_friendship("Enter the name here :")