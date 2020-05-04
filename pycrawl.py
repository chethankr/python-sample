import eventlet
#from eventlet.green import urllib3
import urllib3

urls = [
    "http://www.google.com/intl/en_ALL/images/logo.gif",
    "https://wiki.secondlife.com/w/images/secondlife.jpg",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


#def fetch(url):
#    return urllib3.urlopen(url).read()

def fetch(url):
    httpr = urllib3.PoolManager()
    r = httpr.request('GET', url)
    print(r.status)
    #print(r.data)
    return r.data

pool = eventlet.GreenPool()

for body in pool.imap(fetch, urls):
    print("got body", len(body))