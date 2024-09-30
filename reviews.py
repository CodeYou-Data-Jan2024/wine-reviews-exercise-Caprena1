import pandas as pd

reviews = pd.read_csv('data/winemag-data-130k-v2.csv', index_col=0)

#count = reviews.rename(columns={'description' : 'count'}).sum()

counts = reviews[['country']].value_counts()#.rename(columns={'description' : 'count'}).sum()

counts_reviews = counts.to_frame().reset_index()
counts_reviews.columns = ['country', 'count']
#points = counts_reviews.groupby(['country', 'count', 'points'])

#counts_reviews = points.iloc['points']


print(counts_reviews)

