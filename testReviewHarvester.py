'''Here we want to produce a module that can be used by our processor. This should be
callable with the Steam URL as an input, and will output reviews.'''

'''To prevent an injection attack, make sure that the input is as a string possibly by the module calling this.
gather information to add to database such as game name, etc.'''

import requests    #https://docs.python-requests.org/en/latest/ for API requests with py
import pandas as pd

#def get_AppId(url): maybe with a Regex command.
#Consider inputing app ID to review harvester, seperate module for seperating/sanitzing that.

def ReviewHarvester(): #Here we should have URL as our input.
    
    
    '''We need to pull our appid from the url to input into the requests.get with a format method call?''' 
    
    url = input("Enter your Steam Game URL here... ")
    GameName = (url.split('/')[-2])
    GameID = (url.split('/')[-3])
    print(GameID, GameName)
    
    #print(url)
    return(requests.get('https://store.steampowered.com/appreviews/1635590?json=1').json()) #function adds in appin
    #review_df = pd.read_json(requests.get('https://store.steampowered.com/appreviews/1635590?json=1').json())

#https://store.steampowered.com/appreviews/<AppId>?json=1
    #https://partner.steamgames.com/doc/store/getreviews <-- Steam API Page
    
    #print(reviews)
    #return reviews json file.

#store url and Review output into database

#https://store.steampowered.com/app/1635590/My_Friend_Peppa_Pig/print(type(ReviewHarvester()))
print(ReviewHarvester())

#pandas to read_json()