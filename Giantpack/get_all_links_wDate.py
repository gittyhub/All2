import re
import get_page

#--------------gets all links without query craigslist wanted or SF bay area in it
def get_url_wDate(l,q):
  for x in l:
    if q in get_page.get_page(x): #grabs all links with 5/15 in the page, but probably grabbing it from the title tag and if not in the body, it will get picked up but your prog wont find it if is only looking in the body, so you may need another function that looks for the price in the title with 5/15 so you dont get completly stuck causing exceptioin
        index_site.append(job)
    else:
      continue
  return index_site

