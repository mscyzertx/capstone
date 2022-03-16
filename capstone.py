from http import client
import imp
from turtle import pos
from praw.models import MoreComments
import praw
import pandas as pd

reddit = praw.Reddit(client_id='qXAAG1h8DPJGPFcpuNxe7g',
                     client_secret='8Iq6YfuY70tlfPJpQf_nUDHJO3rciw',
                     user_agent='Capstone Web Scrapping')


#for mutilple subreddit
#subreddit = reddit.subreddit('college+AskReddit+gapyear+lifecoaching+needacoach+socialskills+selfimprovement+softskills')   

subreddit = reddit.subreddit('college')   

# posts

posts = subreddit.top("month")

# for hot posts
# posts = subreddit.hot("month")


#for new posts
#posts = subreddit.new("month")

#<---- Block 1----->
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }



#<---- Block 2-----> 
for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Description
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    #score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)
 
# Saving the data
#<---- Block 3----->
top_posts = pd.DataFrame(posts_dict)
top_posts
top_posts.to_csv("TopPostsMonth.csv", index=True)


#<---- Block 4----->
url ='https://www.reddit.com/r/college/comments/smxnrc/please_help_a_brother_out/'

submission = reddit.submission(url=url)

# for comment in submission.comments:
#     if type(comment) == MoreComments:
#         continue
#     print(comment.body)
#     print()

# submission.comments.replace_more(limit=None)
# comment_queue = submission.comments[:]  
# while comment_queue:
#     comment = comment_queue.pop(0)
#     print(comment.body)
#     comment_queue.extend(comment.replies)

# Comments
#<---- Block 6----->
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)
