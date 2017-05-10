
import urllib2
import re

def getPrice():
    url = raw_input("Please, enter a hepsiburada.com link.")
    try:
        response = urllib2.urlopen(url)
        # Reads html response
        html = response.read() 
        # Regex for price matching html gives prices this pattern (digit...digit(.)digitdigit) -> 12.90
        price_found = a.search("id=\"offering-price\" content=(\d*.?\d*)", html)
        if price_found:
            print price_found.group(1)
        else:
            print "Price not found"
    except Exception as e:
        print e
        pass

cont = raw_input("Do you search a link? ('y' for yes, 'n' for no)")
while cont == 'y':
    getPrice()
    cont = raw_input("Do you search a link? ('y' for yes, 'n' for no)")
