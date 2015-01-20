import check
import Modules_List
import sys
import re

if __name__=='__main__':

  date1 = sys.argv[1].split('/')
  site = 'http://sfbay.craigslist.org/search/sss?sort=rel&query=giants%20+'+date1[0]+'%2F'+date1[1]+'&minAsk=&maxAsk=&sort=date'
  i = int(check.x(5))# this line is just to check so you should see 15 when you run it
  print(i)
  siter = Modules_List.get_AllLinks1(site, sys.argv[1])
  print(siter)
  # monies = Modules_List.find_n_sort_monies(siter, sys.argv[1])
  #print(monies)
  #hope this works
