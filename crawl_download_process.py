from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext
from textblob import TextBlob

class Polly(Crawler):
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer
        html = download(link.url)
        blob = TextBlob(plaintext(html))
        print blob.noun_phrases

    def fail(self, link):
        print 'failed:', repr(link.url)


p = Polly(links=['http://www.cnn.com/'], delay=1)
while not p.done:
       try:
           p.crawl(method=2, cached=False, throttle=1)
           break
       except ValueError:
           print "Encountered error crawling link"