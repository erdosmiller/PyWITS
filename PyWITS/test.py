import re
import string
from BeautifulSoup import BeautifulSoup
from PyWITS.Objects import RecordType

wits_records_file = file('WITSRecords.htm','r')

soup = BeautifulSoup(wits_records_file.read())

tables = soup.findAll('table')

info_tables = []

data_tables = []

x = 1
for i in range((len(tables)-1)/2):
    info_tables.append(tables[x])
    x += 1
    data_tables.append(tables[x])
    x += 1


record_types = []

new_record_type = RecordType.RecordType()

td = info_tables[0].findAll('td')

new_record_type.id = int(td[0].contents[1])
new_record_type.logical_record_type = int(td[1].contents[1])
print td[2]
print td[2].contents[1]
print td[3]
print td[3].contents[1]

myStr = td[4].contents[1]
myStr = myStr.replace('\n','')
myStr = myStr.replace('\t','')
myStr = myStr.replace('\r','')

new_record_type.data_source = myStr

print new_record_type

#    tags = td.contents[0].contents
#    print tags
    #print no_html_re.match(str(td.contents[0])).groups()    

    
    
    
    

