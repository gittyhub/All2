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
  #post_date = re.search('(?<=Posted:).*?</date', From_Site)
  post_date = re.search('(?<=Posted: <date title=".............">).*?<', From_Site) #gets the date of the posting
  if 'mailto' in From_Site: #<< if there is mailto, then return the email address
    return [mail_To.group(), post_date.group()]
  else:
    return ['go to site', post_date.group()]

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


if __name__=='__main__':

  site = 'http://sfbay.craigslist.org/acc/'
  #a = get_jobPosition(site) 
  b = get_email_From_Post(site)
  
  #print(a)
  #print(get_jobPosition(site))
 
  '''for x in get_jobPosition(site):
    if 'go to site' in x:
      print (x)
    else:
      continue'''
  #for x in get_jobPosition(site):
  #  print(x[1] + x[3])

  '''f = open('craigs_jobs', 'w')
  for x in get_jobPosition(site):
    f.write(str(x)+'\n')
  f.close()'''

  '''f = open('craigs_jobs')
  lines = f.readlines()
  a = list([lines[0], 'hello']) 
  print(type(lines[1]))
  print((type(a[0])))
  print(lines[0][0:15]+'2')
  print(lines[0][0])
  #print(lines)
  #print(lines[1].replace('[',''))
  #print(','.split(lines[0]))
  #l1 = lines[0].replace('[','')
  #l1 = l1.replace(']','')
  #l1 = l1.split(',')
  #print(l1)
  #print('E' in l1[1])
  f.close()'''
  
  '''list1 = []
  with open('craigs_jobs','r') as f:
    lines = f.readlines()
    f.close()

  for x in lines:
    list1.append(x)
  print(','.split(list1[0]))'''
