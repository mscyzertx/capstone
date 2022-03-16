from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import praw
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sns.set(style='darkgrid', context='talk', palette='Dark2')


reddit = praw.Reddit(client_id='qXAAG1h8DPJGPFcpuNxe7g',
                     client_secret='8Iq6YfuY70tlfPJpQf_nUDHJO3rciw',
                     user_agent='Capstone Web Scrapping')
                    
posts = set()
for submission in reddit.subreddit('college').new(limit=None):
    posts.add(submission.title)
    display.clear_output()

sia = SIA()
results = []

for line in posts:
    pol_score = sia.polarity_scores(line)
    pol_score['posts'] = line
    results.append(pol_score)
    pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()
df2 = df[['posts', 'label']]

# df2.to_csv('reddit_posts_labels.csv', mode='a', encoding='utf-8', index=False)
    

            