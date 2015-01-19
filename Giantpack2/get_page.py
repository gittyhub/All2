import urllib
import re
from urllib.request import urlopen
import sys

def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""
  return index_site

if __name__=='__main__':

  url = 'http://www.yahoo.com'
  print(get_page(url))

