import urllib
from urllib.request import urlopen
import re

site = 'http://sfbay.craigslist.org/acc/'
email2 = 'htt://craislist.com/pen/acc/4115850973'


def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""

website = get_page(site)
email_to = get_page(email2) 


index_site = []

#a_href = re.findall('"((http|ftp)s?://.*?)"', website)
a_href1 = re.findall('Account.*?<', website)
a_href2 = re.findall('a href.*?</a>', website)
a_href3 = re.findall('>(/w+)Account(/w+)</a>', website)
a_href4 = re.findall('a href.*?</a>', website)

def get_jobPosition():
  for x in a_href2:
    position = re.search('(?<=.html">).*?</a>',x)
    link = re.search('(?<=a href=").*?.html',x)
    if position != None:
      q = [position.group()[0:1],position.group()[:-4],'http://www.craigslist.com'+link.group()]
      index_site.append(q) 
     #index_site.append([h.group()[:-4]])
      #print(h.group()[:-4])
    else:
      continue

def get_email_From_Post:

'''def get_jobPosition():
  for x in a_href2:
    h = re.search('(?<=.html">).*?</a>',x)
    if h != None:
      print(h.group()[:-4])
    else:
      continue'''

'''for x in a_href2:
  h = re.search('(?<=.html">).*?</a>',x)
  if h != None:
    print(h.group()[:-4])
  else:
    continue'''

if __name__=='__main__':
  get_jobPosition()
  print(index_site)


#for x in a_href2:
#   print(a_href2[x])

