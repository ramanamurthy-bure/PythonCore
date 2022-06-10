# Web Scraping is a general term for techniques involving automating the gathering of data from a website
# In this section we will learn how to use Python to conduct web scraping tasks such as downloading the images
# or information off a website

# Rules of Web Scraping
# 1. Always try to get permission before scraping
# 2. If you make too many scraping attempts or requests your IP address could get blocked
# 3. Some sites automatically block scraping software

# Limitations of Web Scraping
# In general every website is unique, which means every web scraping is script is unique
# A slight change or update to a website may completely break your web scraping 


# When viewing a website , the browser doesn't show you all the source code behind the website instead it shows
# you the HTML and some CSS and JS that the website sends to your browser

# HTML is used to create the basic structure and content of a webpage
# CSS is used for the design and style of web page, where elements are placed and how it looks
# JavaScript is used to define the interactive elements of webpage

# For effective basic web scraping we only need to have a basic understanding of HTML and CSS
# Python can view these HTML and CSS elements programmatically, and then extract information from the website
# Let's explore HTML and CSS in more detail

# HTML is Hypertext Markup Language and is present on every website on the internet
# You can right-click on a website and select 'View Page Source' to get an example

# Directly in your command line
# pip install requests
# pip install lxml
# pip install bs4


import requests
import bs4
import lxml
results = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
print(results)
#print(results.text)

soup = bs4.BeautifulSoup(results.text,"lxml")
# Grabbing the entire HTML source in readale format
#print(soup)
# Grabbing the title tag
print(soup.select('title'))
# Grabbing the title text
print(soup.select('title')[0].getText())
# Grabbing all the paragraph tags as list
#print(soup.select('p'))
# Grabbing the second paragraph tag from the list
print(soup.select('p')[1])
# Grabbing the second paragraph text from the list
print(soup.select('p')[1].getText())
# Grabbing the h1 tag
print(soup.select('h1'))

# Syntax                                Match Results
# soup.select('div')                    All elements with 'div' tag
# soup.select('#some_id')               Elements containing id='some_id'
# soup.select('.some_class')            Elements containing class ='some_class')
# soup.select('div span')               Any elements named span within a div element
# soup.select('div > span')             Any elements named span directly within a div element, with  nothing in between








