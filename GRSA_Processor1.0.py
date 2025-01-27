'''This is the main processor core for our GRSA1.0 software.'''

#UI URL request input should be input as string.

#Module that pulls app ID from url input and passes it to review harvester
#Call Review harvester
import testReviewHarvester as tRH
import pandas as pd


review_df = pd.read_json(tRH.ReviewHarvester())

#review_json = pd.read_json(review_json.json)
#review_json.to_excel(DATAFILE.xlsx) #attempt to convert .json to .xlsx file.
'''We converted our .json file to an xlsx file for an easier to work with '''

#Out put review harvester to dataframe pd.read_json(Review Output)

#Using dataframe as input and output, run SA and measure results.
#clean SA results.
#Create DB object and input into Game DB based on the URL.
#Output top/bottom reviews or 'sentiments'? Could use a word cloud or list?
#pass json data into dataframe? so URL key, then json data? 
#Graph of review data?
#Send Output to UI.

