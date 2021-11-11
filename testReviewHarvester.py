'''Here we want to produce a module that can be used by our processor. This should be
callable with the Steam URL as an input, and will output reviews.'''

'''To prevent an injection attack, make sure that the input is as a string possibly by the module calling this.
gather information to add to database such as game name, etc.'''

import requests    #https://docs.python-requests.org/en/latest/ for API requests with py
import pandas as pd
import json
import io
import sys
sys.stdout.encoding

#Can I add an image scraper to this?
url= input("Add your Steam URL here:")
GameName = (url.split('/')[-2])
GameID = (url.split('/')[-3])
print(GameID, GameName)

'''Review Harvester Function pulls reviews from one game/url at a time.'''
def ReviewHarvester():
    
    '''https://store.steampowered.com/appreviews/<AppId>?json=1 <-- API URL
    https://partner.steamgames.com/doc/store/getreviews <-- Steam API Documentation'''
    
    payload = {'language': 'english'}
    r = requests.get(url=f'https://store.steampowered.com/appreviews/{GameID}?json=1', params=payload)
    
    '''Return an error code if request unsuccessful'''
    if r.status_code != 200: 
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
    
    print(type(r))
    

    data=r.json()
    print(type(data))
    del data['success']
    del data['query_summary']
    del data['cursor']
    #del data['recommendationid']
    #del data['author']
    #del data['language']
    #del data['timestamp_created']
    print(data)

    reviews = pd.DataFrame.from_dict(data)
    print(reviews.head(3))
    print(type(reviews))
    
    
ReviewHarvester()

