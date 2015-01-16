import urllib
from urllib.request import urlopen
import re
import sys

#--------gets the page-------
def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""
  return index_site

#--------------gets all links without query craigslist wanted or SF bay area in it
def get_AllLinks1(x,q): #x is the site, and q is the date
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links, and title of the links 
  for x in a_href2:
    if not ('query' in x or 'craigslist' in x or 'SF bay area' in x or 'wanted' in x):
      link = re.search('(?<=a href=").*?.html',x) #<< gets the linke of the job, without the a href's
      job =  'http://sfbay.craigslist.com'+link.group() #attachs the http start to the link completing the hyperlink 
      if q in get_page(job): #grabs all links with 5/15 in the page, but probably grabbing it from the title tag and if not in the body, it will get picked up but your prog wont find it if is only looking in the body, so you may need another function that looks for the price in the title with 5/15 so you dont get completly stuck causing exceptioin
        index_site.append(job)
      else:
        continue
    else:
      continue
  return index_site

#-----------from all the links, find $ amount, sort and display link--------------------------
def find_n_sort_monies(l,q):
  lel_sec = ('level', 'section')
  u = []
  for x in l:
    each = str(get_page(x))
    if '$' in each:
      db = each[each.find('postingbody'):each.find('</section>',each.find('postingbody')+1)] #finds the posting body tag, then finds the section tags that ends the posting body. Stores the body in the var db
      d1 = db.find(q); # find 5/16 in the repost of the tile
      d4 = db.find('$', d1+1) # TARGET : find $ sign
      d7 = db[d4+1:d4+4] #get 4 spaces after the dollar sign
      for i in lel_sec:
        if i in db:
          sec = db.find(i)
          u.append(db[sec:sec+15])
        else:
          u.append(x) 
      try:
        d6 = re.match('.*?([0-9])+',d7).group(0) #.*? starts at the beging not greedy, numbers, + until end or more than one 
      except AttributeError:
        continue     
    else:
      continue
  return u

if __name__=='__main__':

  date1 = sys.argv[1].split('/')
  #site = 'http://sfbay.craigslist.org/search/sss?query=giants%20'+date+'%20club&sort=rel'
  #site = 'http://sfbay.craigslist.org/search/sss?sort=rel&query=giants%20'+date1[0]+'%2F'+date1[1]+'%20club'
  site = 'http://sfbay.craigslist.org/search/sss?sort=rel&query=giants%20+'+date1[0]+'%2F'+date1[1]+'&minAsk=&maxAsk=&sort=date'
  #git = get_page(site) #<-----Test if get_page works
  #print(git)
  siter = get_AllLinks1(site, sys.argv[1]) #grabs all links for the above site with 5/15 in it but you may run into a situation where its in the title and not body, what about 5/15-5/18
  #print(siter) #<----- Test if siter works 
  k = find_n_sort_monies(siter, sys.argv[1]) 
  print(k)
  print(len(k))
