import sys
import re
import urllib2
def todaynotice(date,the_page):
  z=0
  y=0
  l=-1
  print "********************************************************************************"
  print "notice of given date %s is"%date
  print "********************************************************************************"
  while 1:
    m= re.search(';return false">(?=(\w)|(\s\w))', the_page[z:])
    s= re.search('<font class=text>(?=\d)', the_page[y:])
    if not m:
      break
    t= re.search('Hrs</td>', the_page[y:])
    n= re.search('</a></td></tr>', the_page[z:])
    if the_page[y+s.end():y+s.end()+2]==date:
       print the_page[y+s.end() : y+t.start()+3]+"\t\t"+ the_page[z+m.end() : z+n.start()]+"\n\n"
       l=l+1;
    z+=n.end()
    y+=t.end()
  if l<0 :
    print "sorry!!! not available"  
  print "**********************************************************************************"    
def main():
  print "Getting http request..."
  req=urllib2.Request('http://tp.iitkgp.ernet.in/notice/')
  print "Request successful"
  print "Opening url.."
  response=urllib2.urlopen(req)
  print "readin source.."
  the_page=response.read()
  print"*************************************************************************************"
  print"\t\t\t\tNOTICES:"
  print"*************************************************************************************"
  z=0
  y=0
  while 1:  
    m= re.search(';return false">(?=(\w)|(\s\w))', the_page[z:])
    s= re.search('<font class=text>(?=\d)', the_page[y:])
    if not m:
      break
    t= re.search('Hrs</td>', the_page[y:])
    n= re.search('</a></td></tr>', the_page[z:])
    print the_page[y+s.end() : y+t.start()+3]+"\t\t"+ the_page[z+m.end() : z+n.start()]+"\n\n"
    z+=n.end()
    y+=t.end()
  todaynotice(sys.argv[1],the_page)
#if __name__=='__main__':
main()
