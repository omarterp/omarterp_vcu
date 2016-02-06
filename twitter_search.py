from pattern.web import Twitter
from textblob import TextBlob

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('college', start=i, count=30):
        print tweet.id
        print tweet.name
        print tweet.text

        # Pull nouns from tweet
        blob = TextBlob(tweet.text)
        print blob.noun_phrases
        
        print
