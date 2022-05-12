import pandas as pd
from pmaw import PushshiftAPI
api = PushshiftAPI()
import datetime as dt
#before = int(dt.datetime(2011,12,31,0,0).timestamp())
after = int(dt.datetime(2021,1,1,0,0).timestamp())
subreddit="crypto"
q="bitcoin"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, after=after, q=q)
print(f'Retrieved {len(comments)} comments from Pushshift')
comments_df = pd.DataFrame(comments)
# preview the comments data
comments_df.head(5)
comments_df.to_csv('./crypto.csv', header=True, index=False, columns=list(comments_df.axes[1]))