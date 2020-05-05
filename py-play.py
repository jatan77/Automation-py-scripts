from bs4 import BeautifulSoup
import requests

for i in range(34000, 60000):
    url="https://example.com/file/id/"+str(i)+"/data"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    print(soup.title)
    if soup.title.text == "Page not found – KMHD Links":
        print("skipped--"+url+"\n")
    else:
        print("Saved--"+url+"\n")
        file = open('movie-links.txt','a') 
        file.write("\n----------------------------------------------------\n")
        file.write(url+"----"+soup.title.text) 
        file.close() 
