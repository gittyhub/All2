import re

def find_n_sort_monies():
  l = []
  n = 0
  r = open('test2','r')
  e = r.readlines()
  for x in e:
    if '9/9' in x:
      try:
        #dol = re.search('\$\d*', x)
        dol = re.search('(\$\d* | \$\s\d*)', x)
        #idol = re.search('?<=\$)', x)
        #print(dol.group()) 
        #idol3 = dol.group().split('$') 
        dol3 = dol.group().strip('$ ') 
        l.append([int((dol3)),n])
        #l.append([dol3,n])
        #il.append([dol3[1],n])
        n += 1
      except AttributeError:
        n += 1 
  t = (sorted(l))
  for u in t:
    print(u)
  print(len(t))
 
if __name__=='__main__':
  find_n_sort_monies()
 
