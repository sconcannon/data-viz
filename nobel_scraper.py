#! python2
# nobel_scraper.py will scrape a list of Nobel Prize winners from a Wikipedia page.
# from ch 5 of Data Visialization With Python and Javascript

from bs4 import BeautifulSoup
import requests
import lxml


BASE_URL = 'https://en.wikipedia.org'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_Nobel_soup():
    """ Return a parsed tag tree of our Nobel prize page """
    # Make a request to the Nobel page, setting valid headers
    response = requests.get(BASE_URL + '/wiki/List_of_Nobel_laureates', headers=HEADERS)
    # Return the content of the response parsed by BeautifulSoup
    return BeautifulSoup(response.content, features="lxml")

def get_column_titles(table):
    """ Get the Nobel categories from the table header """
    cols = []
    for th in table.select_one('tr').select('th')[1:]:
        link = th.select_one('a')
        # Store the category name and any Wikipedia link it has
        if link:
            cols.append({'name':link.text,'href':link.attrs['href']})
        else:
            cols.append({'name':th.text, 'href':None})
    return cols

def get_Nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for row in table.select('tr')[1:-1]:
        year = int(row.select_one('td').text[:4]) # Gets 1st <td>
        for i, td in enumerate(row.select('td')[1:]):
            for winner in td.select('a'):
                href = winner.attrs['href']
                if not href.startswith('#endnote'):
                    winners.append({
                        'year':year,
                        'category':cols[i]['name'],
                        'name':winner.text,
                        'link':winner.attrs['href']
                    })
    return winners

def get_url(url):
    """ use requests to downlaod a web page """
    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url , headers=HEADERS)
    return BeautifulSoup(response.content)

def get_winner_nationality(w):
    """ scrape biographic data from the winner's wikipedia page """
    soup = get_url('https://en.wikipedia.org' + w['link'])
    person_data = {'name': w['name']}
    attr_rows = soup.select('table.infobox tr')
    for tr in attr_rows:
        try:
            attribute = tr.select_one('th').text
            if attribute == 'Nationality':
                person_data[attribute] = tr.select_one('td').text
        except AttributeError:
            pass
    return person_data