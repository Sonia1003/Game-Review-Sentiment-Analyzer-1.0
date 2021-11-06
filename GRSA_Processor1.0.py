'''This is the main processor core for our GRSA1.0 software.'''

#UI URL request input should be input as string.

import testReviewHarvester as tRH
import SentimentAnalyzer as SA
import pandas as pd


Analysis = SA()
print(Analysis)

 #   review_df = pd.read_json(GetReviews())
#print(head.review_df(2))
#review_df.head(2)

#review_json = pd.read_json(review_json.json)
#review_json.to_excel(DATAFILE.xlsx) #attempt to convert .json to .xlsx file.
'''We converted our .json file to an xlsx file for an easier to work with '''

#Out put review harvester to dataframe pd.read_json(Review Output)

#Using dataframe as input and output, run SA and measure results.
#clean SA results.
#Save into the game's DB object and input into Game DB based on the URL.

#Output top/bottom reviews or 'sentiments'? Could use a word cloud or list?
#pass json data into dataframe? so URL key, then json data? 
#Graph of review data?
#Send Output to UI.


