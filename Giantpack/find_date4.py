import re

def find_n_sort_monies():
  l = []
  n = 0
  r = open('test2','r')
  e = r.readlines()
  for x in e:
    if '9/9' in x:
      try:
        dol = re.search('(\$\d* | \$\s\d*)', x)
        dol3 = int(dol.group().strip('$ '))
        dol4 = re.search('/\w+/tix/\w+',x)
        sec = re.search('Section\s\d*', x)
        #l.append([dol3,n,'http://sfbay.craigslist.org',sec.group()])
        #l.append([dol3,n,'http://sfbay.craigslist.org'+dol4.group()+'.html',sec.group()])
        l.append([dol3,n,'http://sfbay.craigslist.org'+dol4.group()+'.html'])
        n += 1
      except AttributeError:
        n += 1 
  t = (sorted(l))
  for u in t:
    print(u)
  print(len(t))
   
if __name__=='__main__':
  find_n_sort_monies()
   
