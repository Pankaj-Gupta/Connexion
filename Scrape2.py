import string


import urllib2
import re

nameOf1 = 'Sridevi'
nameOf2 = 'Anil_Kapoor'

str1 = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles="+ nameOf1 +"&rvsection=0"
str2 = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles="+ nameOf2 +"&rvsection=0"
url1 = urllib2.urlopen(str1);
url2 = urllib2.urlopen(str2);

orig = url1.read();
#print orig;
#print type(k);
rela = ["SPOUSE", "CHILD", "RELATIVE", "NAME"]
help1_relation = []
help2_relation = []
size = 4
list_1 = [[] for x in range(size)]
list_2 = [[] for x in range(size)]

for main_number in range(1,3):
        if main_number==1:
                url1 = urllib2.urlopen(str1);
                orig = url1.read();
        else:
                url2 = urllib2.urlopen(str2);
                orig = url2.read();

        pos1 = orig.find('Infobox')
        #print pos1;
        temp = orig[pos1:];
        pos2 = temp.find("'''");

        #print pos2;
        info_text = orig[pos1:pos2+pos1]

        #print info_text;


        pos_name = info_text.find('name');
        if(pos_name != -1):
                #print("NAME :"),
                name = info_text[pos_name + len('name ='):]
                for i in range(len(name)):
                    if ord(name[i])>=65 and ord(name[i])<=90:
                        break;
                name = name[i:  (name.find('n|')) -1 ]

                #name = format_name(info_text[pos_name+7:], len(info_text[pos_name+7:]))
                #print name
                if main_number==1:
                        list_1[3].append(name)
                else:
                        list_2[3].append(name)
                #name = info_text[:  (info_text[pos_name:].find('n|'))]
                #print name[0:len(name)-1]
                #print name[0:len(name)-1]




        pos_relative = info_text.find('relatives');
        if(pos_relative != -1):
                #print("RELATIVE :"),
                #print pos_relative + len('relatives =')
                #print (info_text[pos_relative:].find('n|')) + pos_relative + 100
                relative = info_text[pos_relative + len('relatives ='):  (info_text[pos_relative:].find('n|')) + pos_relative+ 100]
                #assuming maximum 4 relatives
                #print relative
                n1 = relative.find('[[');
                n2 = relative.find(']]');
                #print relative[n1+2:n2]
                if main_number==1:
                        list_1[2].append(relative[n1+2:n2])
                        sk1 = relative.find("(");
                        sk2 = relative.find(")");
                        help1_relation.append(relative[sk1+1:sk2])

                else:
                        list_2[2].append(relative[n1+2:n2])
                        sk1 = relative.find("(");
                        sk2 = relative.find(")");
                        help2_relation.append(relative[sk1+1:sk2])
                if n2!=-1:
                    relative = relative[n2+2:]
                    n1 = relative.find('[[');
                    n2 = relative.find(']]');
                    #print relative[n1+2:n2]
                    if main_number==1:
                        list_1[2].append(relative[n1+2:n2])
                        sk1 = relative.find("(");
                        sk2 = relative.find(")");
                        help1_relation.append(relative[sk1+1:sk2])
                    else:
                        list_2[2].append(relative[n1+2:n2])
                        sk1 = relative.find("(");
                        sk2 = relative.find(")");
                        help2_relation.append(relative[sk1+1:sk2])
                #print relative[0:len(relative)-1]



        pos_spouse = info_text.find('spouse');
        if(pos_spouse != -1):
                #print("SPOUSE :"),
                spouse = info_text[pos_spouse + len('spouse ='):  (info_text[pos_spouse:].find('n|')) + len('spouse =')+pos_spouse]
                n1 = spouse.find('[[');
                n2 = spouse.find(']]');
                #print spouse[n1+2:n2]
                if main_number==1:
                        list_1[0].append(spouse[n1+2:n2])
                else:
                        list_2[0].append(spouse[n1+2:n2])
                


        regex = r'[' + "*" + r']';

        pattern = re.compile(regex)
        pos_parents = info_text.find('parents');
        if(pos_parents != -1):
                #print("PARENTS :"),
                parents = info_text[pos_parents + len('parents ='):  (info_text[pos_parents:].find('n|')) + pos_parents]
                
                n1 = parents.find('[[');
                n2 = parents.find(']]');
                #print parents[n1+2:n2]
                tit = re.findall(pattern, parents)
                #print tit
                #print parents[0:len(parents)-1]

        pos_children = info_text.find('children');
        if(pos_children != -1):
                #print("CHILDREN :"),
                children = info_text[pos_children + len('children ='):  (info_text[pos_children:].find('n|')) + pos_children]
                n1 = children.find('[[');
                n2 = children.find(']]');
                #print children[n1+2:n2]
                if main_number==1:
                        list_1[1].append(children[n1+2:n2])
                else:
                        list_2[1].append(children[n1+2:n2])

                #print children[0:len(children)-1]

#print "LIST-1",
#print list_1
#print help1_relation
#print "LIST-2",
#print list_2
#print help2_relation

for i in range(size):
        for j in range(size):
                for k in range(len(list_1[i])):
                        for l in range(len(list_2[j])):
                                if list_1[i][k] == list_2[j][l]:
                                    if i==3:
                                        print nameOf1 +   " is " + rela[j] + " of " + nameOf2
                                    elif j==3:
                                        print rela[i] + " of " + nameOf1 +   " is " + nameOf2
                                    else:
                                        print rela[i] + " of " + nameOf1 +   " is " + rela[j] + " of " + nameOf2 




