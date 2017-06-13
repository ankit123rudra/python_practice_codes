import requests
from bs4 import BeautifulSoup

# the URL of the website we want to parse in this case I have taken the NY times url as it its asked in the question.
url = 'http://www.nytimes.com'
data = requests.get(url)
r_html = data.text
soup = BeautifulSoup(r_html)
for story_heading in soup.find_all(class_="story-heading"):    #using the class="story heading" to go through the loop
#distinguishing between the headings having links and thoes not having links
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip()) 
    else: 
        print(story_heading.contents[0].strip())
