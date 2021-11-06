
"""
If you use the VADER sentiment analysis tools, please cite:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""
import nltk
import nltk.data
import xlsxwriter
import pandas as pd
import testReviewHarvester as tRH


Reviews = tRH.ReviewHarvester()

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid

dataset=pd.read_json(Reviews)
#dataset=pd.read_excel('SentimentReviews.xlsx')
#sid=SentimentIntensityAnalyzer()
dataset['polarity scores'] =dataset['Reviews'].apply(lambda x: sid.polarity_scores(x)['compound']) 
print (dataset)

