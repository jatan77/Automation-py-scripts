from urllib.parse import urlparse
from threading import Thread
import http.client, sys
from queue import Queue
import requests
from bs4 import BeautifulSoup

concurrent = 10

def doWork():
    while True:
        url = q.get()
        print(url)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        print((soup.title.text))
        if soup.title.text == "Page not found – KMHD Links":
            print("skipped--"+url+"\n")
        else:
            print("Saved--"+url+"\n")
            file = open('movie-links.txt','a') 
            file.write("\n----------------------------------------------------\n")
            file.write(url+"----"+soup.title.text) 
            file.close() 
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = http.client.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print((status, url))

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    '''
    for url in open('urllist.txt'):
        q.put(url.strip())            #to take urls from txt file
    '''
    for i in range(50000, 60000):
        url="https://example.com/id/file/"+str(i)+""
        q.put(url)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
