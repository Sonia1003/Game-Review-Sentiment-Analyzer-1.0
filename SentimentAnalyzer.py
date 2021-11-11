
"""
If you use the VADER sentiment analysis tools, please cite:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""
import nltk
import nltk.data
import pandas as pd
import testReviewHarvester as tRH
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid

Reviews = tRH.ReviewHarvester()
print(Reviews)

dataset = Reviews

dataset['polarity scores'] = dataset['Reviews'].apply(lambda x: sid.polarity_scores(x)['compound']) 
print (dataset)

