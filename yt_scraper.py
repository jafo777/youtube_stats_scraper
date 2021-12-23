# importing the libraries
from bs4 import BeautifulSoup
import requests
import json
import re


  
# creating function
def scrape_info(url):
      
    # getting the request from url
    r = requests.get(url)
      
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")

    write_file(s.encode())

    #list of all <script> tags
    scripts = s.select("script")

    pattern = re.compile(r"responseContext\s+=\s+(\{.*?\});\n")
    script = s.find("script", text=pattern)
    print(script)

  
    if "responseContext" in scripts[19].string:
        print("YEPPPPJOASIFJASLFKJ!")
        json_data =json.loads(scripts[19].string)
        print(json_data)
    for i in scripts:
        if "responseContext" in i.string:
            print('YEP!!!!!!')



    # print(s.findAll('script'))
      
    # # finding meta info for title
    # title = s.find("span", class_="watch-title").text.replace("\n", "")
      
    # # finding meta info for views
    # views = s.find("div", class_="watch-view-count").text
      
    # # finding meta info for likes
    # likes = s.find("span", class_="like-button-renderer").span.button.text
      
    # # saving this data in dictionary
    # data = {'title':title, 'views':views, 'likes':likes}
      
    # returning the dictionary
    # return data

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