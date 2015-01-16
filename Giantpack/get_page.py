import urllib
from urllib.request import urlopen
import sys

def get_page(url):
#def get_page(url=None):
#  try:
#    url = sys.argv[1]
#  except IndexError:
#    "" 
#  if url is None:
#    url = 'http://www.yahoo.com'
  try:
    return str(urlopen(url).read())
  except:
    return ""
  return index_site

if __name__=='__main__':
  
  print(get_page())

