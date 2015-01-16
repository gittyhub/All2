import urllib 
from urllib.request import urlopen

cjob_main = 'https://sfbay.craigslist.org/acc'

def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""

def find_item():
  p = get_page(cjob_main) 
  return p

#print(get_page(energizer_qi))
print(find_item())
