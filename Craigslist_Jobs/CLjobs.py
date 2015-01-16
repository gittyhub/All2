import mechanize
import sys
import linecache
import urllib

cList='https://sfbay.craigslist.com/acc/'

"""nexus_site='http://www.google.com'"""

def get_date(x):
  b = mechanize.Browser()
  fd = b.open(x)
  price = fd.read()
  
#  print(price)

 
if __name__=='__main__':
  get_date(Clist)


