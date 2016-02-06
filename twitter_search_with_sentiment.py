from pattern.web import Twitter
from textblob import TextBlob

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('college', start=i, count=30):
        print tweet.id
        print tweet.name
        print tweet.text

        blob = TextBlob(tweet.text)
        # Pull nouns from tweet
        print blob.noun_phrases
        # tweet's sentiment analysis
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)

        print
