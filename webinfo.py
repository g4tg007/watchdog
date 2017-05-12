# encoding: utf-8
import urllib
import re
import sgmllib
from bs4 import BeautifulSoup


class handle_html():
 
 def read_page(self,url):
    web=urllib.urlopen(url)
    page=web.read()
    return page

 def read_page_link(self,page,lens):
    soup = BeautifulSoup(page,"lxml")
    links=[]
    for hrefs in soup.find_all('a'):
        links.append(hrefs.get('href'))
    if lens==1:
    	return len(links)
    else:
    	return links
    pass

 def if_login(self,page):
    re_1 = re.search('login',page)
    if re_1:
        return 1
    else:
        return 0
    pass



if __name__ == '__main__':
    
   web_handler = handle_html()
   page=web_handler.read_page("http://erp.jd.com")
   print web_handler.read_page_link(page,1)
   print web_handler.if_login(page)

#tags_a =soup.findAll(name="a",attrs={'href':re.compile("^https?://")})

#print tags_a