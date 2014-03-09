import urllib2
import re

nameOf1 = 'Akshay_Kumar'
nameOf2 = 'Sunil_Shetty'

str1 = "http://live.dbpedia.org/page/" + nameOf1
str2 = "http://live.dbpedia.org/page/" + nameOf2
#str2 = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles="+ nameOf2 +"&rvsection=0"



url1 = urllib2.urlopen(str1);
url2 = urllib2.urlopen(str2);

orig1 = url1.read();
orig2 = url2.read();


pos_1 = [m.start() for m in re.finditer('dbpprop:starring', orig1)]
pos_2 = [m.start() for m in re.finditer('dbpprop:starring', orig2)]

l1 = len(pos_1)
l2 = len(pos_2)


movies_1 = ["" for i in xrange(l1)]
movies_2 = ["" for i in xrange(l2)]


#print len(x1)

for i in range(l1):
	pos2 = orig1.find('<small>dbpedia</small>:', pos_1[i]) + len('<small>dbpedia</small>:')
	pos3 = orig1.find('</a>', pos2)
	movies_1[i] = orig1[pos2: pos3]

#print movies_1

for i in range(l2):
	pos2 = orig2.find('<small>dbpedia</small>:', pos_2[i]) + len('<small>dbpedia</small>:')
	pos3 = orig2.find('</a>', pos2)
	movies_2[i] = orig2[pos2: pos3]

#print movies_2


if 1:
	for i in range(l1):
		for j in range(l2):
			if movies_1[i] == movies_2[j]:
				print movies_2[j]










