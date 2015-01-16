import re

def find_n_sort_monies():
  l = []
  n = 0
  r = open('test2','r')
  e = r.readlines()
  for x in e:
    if '9/9' in x:
      try:
        dol = re.search('(\$\d*)',x)# | \$\s\d* | \$\d*/ | \$\d*.)', x) #find all $
        dol2 = dol.group()
        l.append([dol2,n])
        n += 1
      except AttributeError:
        l.append([n])
        n += 1 
    else:
      l.append([n, 'no 9\'s'])
      n += 1 
  print(len(l))
   
if __name__=='__main__':
  find_n_sort_monies()
   
