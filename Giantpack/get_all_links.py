import re

#--------------gets all links without query craigslist wanted or SF bay area in it
def get_AllLinks1(x,q): #x is the site, and q is the date
  index_site = [] #<< creates an empty list
  website = x #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links, and title of the links 
  for x in a_href2:
    if not ('query' in x or 'craigslist' in x or 'SF bay area' in x or 'wanted' in x):
      link = re.search('(?<=a href=").*?.html',x) #<< gets the linke of the job, without the a href's
      job =  'http://sfbay.craigslist.com'+link.group() #attachs the http start to the link completing the hyperlink 
      index_site.append(job)
    else:
      continue
  return index_site

