#new classes
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

#leaving only items of interest
lst1 = list()
lst2 = list()
lst3 = list()
fnum = input("Course file number:")
fname ='Selected Hampshire Courses'+fnum+'.html'
html_file1 = open(fname, encoding = "ISO-8859-1")
source_code1 = html_file1.read()

soup1 = BeautifulSoup(source_code1, 'html.parser')
tags1 = soup1('p')

for tag1 in tags1:
    if re.match('LIST_VAR12_.+',tag1['id']):
        tag1 = tag1.contents[0]
        a = re.findall('(\S+)/\S+/\S+', str(tag1))
        c = re.findall('\S+/(\S+)/\S+', str(tag1))
        w = re.findall('\S+/\S+/(\S+)', str(tag1))
        if not len(c) == 0:
            lst2.append(int(c[0])-int(a[0])+int(w[0]))
            lst3.append(int(c[0]))

#for all names that include first year seminar 'LCSEM'
for tag2 in tags1:
    if re.match('LIST_VAR3_.+',tag2['id']) and re.match('.*LCSEM.*', str(tag2.contents[2])):
        q = re.findall('LIST_VAR3_(\S+)',tag2['id'])
        x = q[0]
        for tag3 in tags1:
            if re.match('LIST_VAR12_%s' % x,tag3['id']):
                tag3 = tag3.contents[0]
                a1 = re.findall('(\S+)/\S+/\S+', str(tag3))
                a2 = re.findall('\S+/(\S+)/\S+', str(tag3))
                if not len(a1) == 0:
                    lst1.append(int(a2[0])-int(a1[0]))

print('Number of first years in FYSs: ', sum(lst1))
print('Number of classes signed up: ', sum(lst2))
print('Total number of classes: ', len(lst3))
print('Total space in classes: ', sum(lst3))
