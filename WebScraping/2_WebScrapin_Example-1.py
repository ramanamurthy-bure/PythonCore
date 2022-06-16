import requests
import bs4
import lxml

home_page = 'http://books.toscrape.com/index.html'
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
two_star_titles = []
result = ""

for i in range(0,51):
    if i == 0:
        result = requests.get(home_page)
    else:
        page_url = base_url.format(i)
        result = requests.get(page_url)

    soup = bs4.BeautifulSoup(result.text, "lxml")
    # print(soup)
    book_products = soup.select('.product_pod')
    for book in book_products:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print("Total Books with 2 star rating: ",len(two_star_titles))
print("Book titles are : \n")
for x in two_star_titles:
    print(x)








