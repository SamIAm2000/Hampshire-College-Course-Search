#new classes
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

#leaving only items of interest
lst1 = list()
lst2 = list()

fnum1 = input('Course 1:')
fnum2 = input('Course 2:')
fname1 = 'Selected Hampshire Courses' +fnum1+'.html'
fname2 = 'Selected Hampshire Courses'+fnum2+'.html'

html_file1 = open(fname1, encoding = "ISO-8859-1")
html_file2 = open(fname2, encoding = "ISO-8859-1")
source_code1 = html_file1.read()
source_code2 = html_file2.read()

soup1 = BeautifulSoup(source_code1, 'html.parser')
soup2 = BeautifulSoup(source_code2, 'html.parser')
tags1 = soup1('p')
tags2 = soup2('p')

for tag1 in tags1:
    if re.match('LIST_VAR3_.+',tag1['id']):
        tag1 = tag1.contents[0]
        lst1.append(tag1)

for tag2 in tags2:
    if re.match('LIST_VAR3_.+',tag2['id']):
        tag2 = tag2.contents[0]
        lst2.append(tag2)

difference = set(lst1).symmetric_difference(set(lst2))
final = list(difference)
final.sort()
for item in final:
    print(item)
