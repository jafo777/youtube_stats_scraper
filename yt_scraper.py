# importing the libraries
from bs4 import BeautifulSoup
import requests
  
# creating function
def scrape_info(url):
      
    # getting the request from url
    r = requests.get(url)
      
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")

    write_file(s.encode())

    print(s.prettify())
      
    # finding meta info for title
    title = s.find("span", class_="watch-title").text.replace("\n", "")
      
    # finding meta info for views
    views = s.find("div", class_="watch-view-count").text
      
    # finding meta info for likes
    likes = s.find("span", class_="like-button-renderer").span.button.text
      
    # saving this data in dictionary
    data = {'title':title, 'views':views, 'likes':likes}
      
    # returning the dictionary
    return data

def write_file(text):
    # Opening a file
    file1 = open('html_output.html', 'w')

    # Writing a string to file
    file1.write(text)
  
# main function
if __name__ == "__main__":
      
    # URL of the video
    url ="https://www.youtube.com/watch?v=ffcitRgiNDs"
      
    # calling the function
    data = scrape_info(url)
      
    # printing the dictionary
    print(data)