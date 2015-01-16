#import check
#import Modules_List
import sys
import re
import get_page
import get_all_links
import get_all_links_wDate

if __name__=='__main__':

  index_site = []
  date1 = sys.argv[1].split('/')
  #url = 'http://sfbay.craigslist.org/search/sss?sort=rel&query=giants%20+'+date1[0]+'%2F'+date1[1]+'&minAsk=&maxAsk=&sort=date'
  #url = 'http://sfbay.craigslist.org/search/sss?query=giants%20+'+date1[0]+'%2F'+date1[1]+'sort=rel'
  #url = 'http://sfbay.craigslist.org/search/sss?query=giants'+date1[0]+'%2F'+date1[1]+'&sort=rel'
  url = 'http://sfbay.craigslist.org/search/sss?query=giants+9%2F9&sort=rel'
  get_url_source = get_page.get_page(url)
  f = open('test','w')
  f.write(get_url_source)
  f.close()
  f = open('test','r')
  read_line_as_string_in_text = str(f.readlines())
  get_all_link_from_test = get_all_links.get_AllLinks1(read_line_as_string_in_text, date1)
  remove_dup = list(set(get_all_link_from_test))
  '''for x in remove_dup:
    index_site.append(x)'''
  t = open('test2','a')
  num = range(len(remove_dup))
  for x in num:
    if sys.argv[1] in get_page.get_page(remove_dup[x]):
      t.write(get_page.get_page(remove_dup[x]))
      t.write('\n')
      #print(str(x)+'yes')
    else:
      continue 
      #print(str(x)+'no')
  #print(sys.argv[1] in get_page.get_page(x))
  #q = open('test1','w')
  #q.write(str(get_all_link_from_test))
  #dig = get_all_links_wDate.get_url_wDate(get_all_link_from_test, date1)  

 
  #print(set(get_all_link_from_test))
  #f.close()
