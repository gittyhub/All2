import re

#def find_n_sort_monies(l,q):
def find_n_sort_monies():
  f = open('test2','r')
  #f.readlines()
  q = str(f.readlines())
  return(q)
 
if __name__=='__main__':
#-----------from all the links, find $ amount, sort and display link-------------------------p-

  r = open('test2','r')
  p=(str((r.readlines())))
  r.close()
  #print(find_n_sort_monies())

 
  u = []
  for x in l:
    each = str(get_page(x))
    if '$' in each:
      db = each[each.find('postingbody'):each.find('</section>',each.find('postingbody')+1)] #finds the posting body tag, then finds the section tags that ends the posting body. Stores the body in the var db
      d1 = db.find(q); # find 5/16 in the repost of the tile
      d4 = db.find('$', d1+1) # TARGET : find $ sign
      d7 = db[d4+1:d4+4] #get 4 spaces after the dollar sign
      #if not('level' in db or 'section' in db):
      #if 0 < db.lower().find('row'):
      if 'Row' in db:
        sec = db.lower().find('row')
        u.append(db[sec:sec+20])
      #continue
      else:
        print('yo'+' '+x)  
    else:
      continue
  return u
'''
