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
        l.append(dol3,n])
        n += 1
      except AttributeError:
        n += 1 
  t = (sorted(l))
  for u in t:
    print(u)
  print(len(t))
   
if __name__=='__main__':
  find_n_sort_monies()
   
