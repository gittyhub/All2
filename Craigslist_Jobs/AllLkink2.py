import urllib
from urllib.request import urlopen
import re

def get_page(url):
  try:
    return str(urlopen(url).read())
  except:
    return ""

def get_email_From_Post(y):
  From_Site = get_page(y)  #open the posting of the job 
  mail_To = re.search('(?<=mailto:).*?.org',From_Site) #<< finds mailto and gets stores the email address if any
  if 'mailto' in From_Site: #<< if there is mailto, then return the email address
    return mail_To.group()
  else:
    return 'go to site'
  #return mail_To

def get_jobPosition(x):
  index_site = [] #<< creates an empty list
  website = get_page(x) #<< opens http://sfbay.craigslist.com/acc
  a_href2 = re.findall('a href.*?</a>', website) #<< from the above, finds all job posting links
  for q in a_href2:
    position = re.search('(?<=.html">).*?</a>',q) #<< name of the position
    link = re.search('(?<=a href=").*?.html',q) #<< gets the linke of the job
    #webby = 'http://sfbay.craigslist.com'+link.group()
    if position != None:
      job =  'http://sfbay.craigslist.com'+link.group()
      email = get_email_From_Post(job)
      r = [position.group()[0:1],position.group()[:-4], job, email]
      #r = [position.group()[0:1],position.group()[:-4], link1, 'http://sfbay.craigslist.com'+link.group()]
      #r = 'http://sfbay.craigslist.com'+link.group()
      index_site.append(r) 
    else:
      continue
  return index_site


if __name__=='__main__':

  site = 'http://sfbay.craigslist.org/acc/'
  email2 = 'http://sfbay.craigslist.org/sfc/acc/4118096507.html'

  #print(get_jobPosition(site)[1][2])
  for x in  get_jobPosition(site): 
    print(x[3])#[0][3])
  #print(get_jobPosition(site)[0][3])
  #print(get_email_From_Post(email2).group())
  #print(get_email_From_Post(email2))
  #webyy = get_jobPosition(site)[1][2]
  #print(webyy)
  #print(get_email_From_Post(webyy)) 


