
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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def SA():
    sia = SentimentIntensityAnalyzer()
    df1 = tRH.ReviewHarvester()
    #print(df1['Reviews'])

    #data['Reviews'] = data['Reviews'].astype(str)
    df2 = df1['Reviews']


    df1['Compound'] = [sia.polarity_scores(x)['compound'] for x in df2]
    df1['Why0neg'] = [sia.polarity_scores(x)['neg'] for x in df2]
    df1['Why0neu'] = [sia.polarity_scores(x)['neu'] for x in df2]
    df1['Why0pos'] = [sia.polarity_scores(x)['pos'] for x in df2]
    print(df1)
    return(df1)
SA()
