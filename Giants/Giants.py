import urllib
from urllib.request import urlopen
import re


#--------gets the page-------
def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""


#--------gets all the <mailto tags and get the posting date----------------
def get_email_From_Post(y):
  From_Site = get_page(y)  #open the posting of the job 
  mail_To = re.search('(?<=mailto:).*?.org',From_Site) #<< finds mailto and gets stores the email address if any
  #post_date = re.search('(?<=Posted:).*?</date', From_Site)
  post_date = re.search('(?<=Posted: <date title=".............">).*?<', From_Site) #gets the date of the posting
  if 'mailto' in From_Site: #<< if there is mailto, then return the email address
    return [mail_To.group(), post_date.group()]
  else:
    return ['go to site', post_date.group()]


#---------gets the name of the postion and link to the job-------------------------
def get_jobPosition(x):
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links 
  for q in a_href2:
    position = re.search('(?<=.html">).*?</a>',q) #<< name of the position with .html> 
    link = re.search('(?<=a href=").*?.html',q) #<< gets the linke of the job
    if position != None:
      job =  'http://sfbay.craigslist.com'+link.group() #first letter of job, job, job links 
      email = get_email_From_Post(job) # gets email address and date
      #post_date = re.search('(?<=Posted:).*?</date', job)
      r = [position.group()[0:1],position.group()[:-4], job] #first part
      for x in email:
        r.append(x)
      index_site.append([r]) 
    else:
      continue
  return index_site

#------------get all ahref and the title of the links
def get_AllLinks(x):
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links, and tile of the links
  for x in a_href2:
    if not ('query' in x or 'craigslist' in x or 'SF bay area' in x or 'wanted' in x):
    #if 'query' or 'craigslist' not in x:
      index_site.append(x) 
    else:
      continue
  return index_site

#--------------gets all links without query craigslist wanted or SF bay area in it
def get_AllLinks1(x):
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href="/.*?</a>', website) #<< from the above, finds all a href links, and title of the links 
  for x in a_href2:
    if not ('query' in x or 'craigslist' in x or 'SF bay area' in x or 'wanted' in x):
      link = re.search('(?<=a href=").*?.html',x) #<< gets the linke of the job, without the a href's
      job =  'http://sfbay.craigslist.com'+link.group() #attachs the http start to the link completing the hyperlink 
      if '6/6' in get_page(job): #grabs all links with 5/15 in the page, but probably grabbing it from the title tag and if not in the body, it will get picked up but your prog wont find it if is only looking in the body, so you may need another function that looks for the price in the title with 5/15 so you dont get completly stuck causing exceptioin
        index_site.append(job)
      else:
        continue
    else:
      continue
  return index_site


if __name__=='__main__':

  site = 'http://sfbay.craigslist.org/search/sss?query=giants%206/6%20club&sort=rel'
  l = get_AllLinks1(site) #grabs all links for the above site with 5/15 in it but you may run into a situation where its in the title and not body, what about 5/15-5/18
  sup = []
  #print(l)
  for x in l:
    each = str(get_page(x))
    if '$' in each:
      d = each.find('postingtitle'); #find repost in page with the title
      d1 = each.find('6/6', d+1 ); # find 5/16 in the repost of the tile
      d2 = each.find('6/6', d1+1) # TARGET : find 5/16 after the repost of title
      d4 = each.find('$', d2+1) # TARGET : find $ sign
      d7 = each[d4:d4+4] #get 4 spaces after the dollar sign
      #if d7 != None:
      try:
        d6 = re.match('.*?([0-9])+',d7).group(0) #.*? starts at the beging not greedy, numbers, + until end or more than one 
        sup.append(d6)
      except AttributeError:
        print('yolo + x')     
      #d6 = re.search('.*?([0-9])+,h
      #d5 = each[d4:d4+4]+ '------>:  ' + x
      #d5 = d6 + '---->  ' + x
      #sup.append(d5)
        #print((d6,x))
        #sup.append(d6)
      #else:
      #  print('YOLO----------> ' + x)
    else:
      continue
  #k = sup.sort()
  #for x in k:
  k = sorted(sup)
  for c in k:
    print(c)
  #print(k) '''

