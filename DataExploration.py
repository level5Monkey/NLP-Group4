# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 21:17:53 2022

@author: Jiaxing Li
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json('./Office_Products_5.json', lines=True)

data.head(3)
data.describe()
data.shape
data.dtypes
data.columns
data.columns.values
data.info()
data.keys()
data.isnull().sum()
data.columns

data['overall'].describe()

# Distribution of the number of reviews per product
productReviewCount = data.groupby(['asin']).size()
productReviewCount.plot.hist(bins=12, alpha=0.5)
plt.xlabel('review count per product')

# Distribution of reviews per user
userReviewCount = data.groupby(['reviewerID']).size()
userReviewCount.plot.hist(bins=12, alpha=0.5)
plt.xlabel('review count per user')

# Distribution of all reviews
review = pd.DataFrame(data.groupby(['overall']).size())
review['rating'] = [1,2,3,4,5]
review.plot(x='rating',kind='bar')
plt.xlabel('rating')

# Distribution of review text length
reviewLength = data['reviewText'].apply(len)
reviewLength.plot.hist(bins=2000, alpha=0.5)
plt.xlabel('length per review')