import os
import json

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

files = os.listdir('/user/research/ptan/data/Twitter')
print(len(files))

movies = open("movi_lst.txt")
movies_lst = []
for line in movies:
    movies_lst.append(line.strip("\n"))



output_file = open("tweet_output4.txt", 'a+')
for f in files:
    tweets = open('/user/research/ptan/data/Twitter/' + f)

    for tweet in tweets:
        try:
            tweet = json.loads(tweet)
        except ValueError:
            continue
        
        try:
            text = tweet['text']
            date = tweet['created_at']
        except KeyError:
            continue
            
        for movie in movies_lst:
            movie = " " + movie + " "
            upper = movie.upper()
            lower = movie.lower()
                    
            if (movie in text) or (upper in text) or (lower in text):
                output_file.write(text + ", " + date + ", " + movie + "\n" )
    
print("All Done") 
