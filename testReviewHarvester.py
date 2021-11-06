'''Here we want to produce a module that can be used by our processor. This should be
callable with the Steam URL as an input, and will output reviews.'''

'''To prevent an injection attack, make sure that the input is as a string possibly by the module calling this.
gather information to add to database such as game name, etc.'''

import requests    #https://docs.python-requests.org/en/latest/ for API requests with py
import pandas as pd


#def get_AppId(url):
#Consider inputing app ID to review harvester, seperate module for seperating/sanitzing that.

def ReviewHarvester(): #Here we should have URL as our input.
    
    
    '''We need to pull our appid from the url to input into the requests.get with a format method call?''' 
    
    #print(url)
    return(requests.get('https://store.steampowered.com/appreviews/1635590?json=1').json())
    #review_df = pd.read_json(requests.get('https://store.steampowered.com/appreviews/1635590?json=1').json())
    #https://store.steampowered.com/appreviews/<AppId>?json=1
    #https://partner.steamgames.com/doc/store/getreviews <-- Steam API Page
    
    #print(reviews)
    #return reviews json file.


print(type(ReviewHarvester()))
print(ReviewHarvester())

#pandas to read_json()