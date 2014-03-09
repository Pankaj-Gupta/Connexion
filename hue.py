import string
import pygame
from pygame.locals import *
import urllib2
import re

nameOf1 = 'Amitabh_Bachchan'
nameOf2 = 'Aishwarya_Rai_Bachchan'




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

#print '\n\n\n'+ "The movies which they have in common are:"
to_print = "                       "
for i in range(size):
        for j in range(size):
                for k in range(len(list_1[i])):
                        for l in range(len(list_2[j])):
                                if list_1[i][k] == list_2[j][l]:
                                    if i==3:
                                        to_print = to_print + nameOf1 +   " is " + rela[j] + " of " + nameOf2
                                    elif j==3:
                                        to_print = to_print + rela[i] + " of " + nameOf1 +   " is " + nameOf2
                                    else:
                                        to_print = to_print +  rela[i] + " of " + nameOf1 +   " is " + rela[j] + " of " + nameOf2 




to_print = to_print +  '                   '+ "The movies which they have in common are:"

if 1:
    for i in range(l1):
        for j in range(l2):
            if movies_1[i] == movies_2[j]:
                to_print = to_print +  movies_2[j] + ','

print to_print
pygame.init()
# Set size of pygame window.
screen=pygame.display.set_mode((640,480))
# Create empty pygame surface.
background = pygame.Surface(screen.get_size())
# Fill the background white color.
background.fill((255, 255, 255))
# Convert Surface object to make blitting faster.
background = background.convert()
# Copy background to screen (position (0, 0) is upper left corner).
screen.blit(background, (0,0))

#to_print = "adsdsfdfbfngngnghghykykm dga sgsf egsdagdgdg ghdhfghrG idon ewskfnd ffsf fsfsfskvnsvskfslfslfa"

mainloop = True
while mainloop:
    # Do not go faster than this framerate.
   
    
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                
    # Print framerate and playtime in titlebar.
    text = "CONNEXION"
    pygame.display.set_caption(text)

    font = pygame.font.Font(None, 45)

    text = font.render(to_print, 1, (10, 10, 10))


    leap = 36
    i=0;
    k=0;
    while 1:
        if leap*(k+1)>=len(to_print):
            text = font.render(to_print[leap*k :], 1, (10, 10, 10))
            background.blit(text, (0, k*25))
            break;

        text = font.render(to_print[leap*k :leap*(k+1)], 1, (10, 10, 10))
        background.blit(text, (0,k*25))
        k = k+1;
        

    screen.blit(background, (0, 0))
    #Update Pygame display.
    pygame.display.flip()

# Finish Pygame.  
pygame.quit()
