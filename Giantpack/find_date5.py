import re

def find_n_sort_monies():
  l = []
  n = 0
  r = open('test2','r')
  e = r.readlines()
  for x in e:
    if '9/9' in x:
      #try:
      dol = re.search('(\$\d* | \$\s\d* | \$\d*/ | \$\d*.)', x) #find all $
        '''dol3 = (dol.group().strip('$./ ')) #change $ to int and splits them
        l.append([dol3,n])
        dol4 = re.search('/\w+/tix/\w+',x) #looks for the ticket tag
        sec = re.search('Section\s\d*', x) #finds section
        #l.append([dol3,n,'http://sfbay.craigslist.org',sec.group()])
        l.append([dol3,n,'http://sfbay.craigslist.org'+dol4.group()+'.html',sec.group()])
        #l.append([dol3,n,'http://sfbay.craigslist.org'+dol4.group()+'.html'])
        dol5 = dol4.group()'''
      n += 1
      '''except AttributeError:
        sec = 'none'
        dol = re.search('(\$\d* | \$\s\d*)', x) #find all $
        if dol == None:
          dol = 'none'
          dol3 = 'none'
        else:
          dol3 = int(dol.group().strip('$ ')) #change $ to int and splits them'''
    else:
      l.appen(n)
      n += 1 
        '''dol4 = re.search('/\w+/tix/\w+',x) #looks for the ticket tag
        #dol5 = dol4.group()
        if dol4 == None:
          dol4 = 'none'
          dol5 = 'none' 
        l.append([dol3,n,'http://sfbay.craigslist.org'+dol5+'.html',sec])
        l.append(['AE',n])
        n += 1 
  #t = (sorted(l))
  for u in l:
    print(u)'''
  print(len(l))
   
if __name__=='__main__':
  find_n_sort_monies()
   
