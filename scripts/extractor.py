# Housekeeping
from bs4 import BeautifulSoup
import pandas
import requests_html


##
# Extractor function that acquires data from a OraclesElixir.com
#
def extract(url):
    # Acquire the data
    session = requests_html.HTMLSession()  # Using requests-html to render javascript
    r = session.get(url)
    r.html.render()
    text = r.html.html
    soup = BeautifulSoup(text, features="html.parser")

    # Acquire download links
    links = soup.select("[download]")

    # Construct return value
    data = {}
    for link in links:
        data[link.string] = pandas.read_csv(link['href'], low_memory=False)

    return data
