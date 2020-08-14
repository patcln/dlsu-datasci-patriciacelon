import pandas as pd 
import datetime
import csv
import os 
import requests 
import datetime as dt
import time


URL = "https://api.pushshift.io/reddit/submission/search/"


author #aggs
subreddit #aggs
date created #sort_type #aggs
number of comments #sort_type
score #sort_type
submission title
submission description


PARAMS = {
    'author':
    'subreddit': 'linglin40hrs',
    'after': 1483228800, #get dates after March 31, 2020
    'before': 1588291200, #get dates before May 1, 2020
    'num_comments':
    'title':
    'sort_type': 'score', # sort by score
    'sort': 'desc', # sort in descending order
    'metadata':
    'size': 20, # give only 20 search results
#     'fields': ["id","title","selftext","score","num_comments","created_utc"] #return only the following fields
}


URL = "https://api.pushshift.io/reddit/submission/search/"  #query submissions
PARAMS = {
    'after': 1483228800, #get dates after March 31, 2020
    'before': 1588291200, #get dates before May 1, 2020
    'sort_type': 'score', # sort by score
    'sort': 'desc', # sort in descending order
    'subreddit': 'lingling40hrs', # do a search on DLSU subreddit
    'size': 20, # give only 20 search results
#     'fields': ["id","title","selftext","score","num_comments","created_utc"] #return only the following fields
}

#use the requests library to query pushshift api
r = requests.get(url = URL, params=PARAMS)
#parse returned data to a json object
r.json()


def to_utc(date):
    #This function converts an object to UTC. This is to automate the conversion 
    #of dates instead of going to https://www.unixtimeconverter.io/ 
    return int(date.replace(tzinfo=dt.timezone.utc).timestamp())
    
def to_readable_date(timestamp):
    #This function converts the UTC format to a Year-Month-Day format 
    return dt.datetime.fromtimestamp(timestamp).strftime("get_ipython().run_line_magic("Y-%m-%d")", "")

#Declare start and end of reddit posts to extract 
start_date = dt.datetime.strptime("2020-04-01", "get_ipython().run_line_magic("Y-%m-%d")", "")
end_date = dt.datetime.strptime("2020-04-05", "get_ipython().run_line_magic("Y-%m-%d")", "")

#Create a range of dates to iterate 
#Note: Periods here represents the number of days it will create from the start date 
#We also do a +2 since it will only generate up to April 29. We inlcude May 1 
#since we want to get data from the last day which is April 30 to May 1 
date_range = (pd.date_range(
                start_date, 
                periods=(end_date - start_date).days + 2)
              .tolist())

#prepare the parameters needed to call the API
sort_type="score"
sort="desc"
fields=["author","subreddit","created_utc","num_comments","score","title","desc"]
#fields=["id","title","selftext","score","num_comments","created_utc"]
subreddit = 'lingling40hrs'
url = "https://api.pushshift.io/reddit/submission/search/"
results = []
#loop through the dates 
for i, s_date in enumerate(date_range):
    #prevents us from getting an index out of range error
    if i get_ipython().getoutput("= len(date_range)-1:")
        #declare end date 
        e_date = date_range[i+1]
        #call the API
        r = requests.get(url = url, params={
            'after': to_utc(s_date),
            'before': to_utc(e_date),
            'sort_type': sort_type,
            'sort': sort,
            'subreddit': subreddit,
            'fields': fields,
            "size": 500
        })

        #add logs 
        print(f"Doing {s_date.strftime('get_ipython().run_line_magic("Y-%m-%d')}", " to {e_date.strftime('%Y-%m-%d')}\")")
        if r.status_code == 200:
            results.append(r.json()['data'])
            print("=====Done")
        else:
            print("=====Skipped")
        #so that we dont get blocked from abusing the API we call it after pausing for 1 second
        time.sleep(1)


results


flat_list = []
#loop through the reddit results
for sublist in results:
    #check if sublist is not empty. The reason we have empty lists is because there are days wherein there are no submissions
    if sublist is not None:
        #for each dictionary in the sublist add it to the flat list 
        for item in sublist:
            flat_list.append(item)

#pandas has a useful function called from_dict which will convert a list of dictionary objects into a dataframe
df = pd.DataFrame.from_dict(flat_list)
display(df.head())
df.to_csv("reddit_twoset.csv")



