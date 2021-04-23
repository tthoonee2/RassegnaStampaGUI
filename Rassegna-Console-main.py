import requests
import feedparser
####THE CODE IS STRUCTURED AS FOLLOWS:
#1. Import and save custom feed links
"""
    a. input of link
    b. request of link - verify get and try exception [200]
    c.add link to a new line in the file.
"""
try:
    file = open('linkssaved.txt', 'w')
except:
    file = open('linkssaved.txt', 'x')
listoflinks = []
choice = input('insert a link? [y/n]\n')
if choice is 'y':
    while choice is 'y':
        new_link = str(input('insert a new link to be added to your favorites: '))
        response = requests.get(new_link)
        print(response)
        response = str(response)
        if response == '<Response [200]>': #loaded the rss, so the link is very much probably valid
            listoflinks.append(new_link)
            choice = input('insert a link? [y/n]\n')
        else:
            choice = input('insert a link? [y/n]\n')
else:
    pass

file.writelines(listoflinks)

file.close()

file = open("linkssaved.txt", 'r')
print('ho aperto il file')

    
    #run the rest of the program


#2.access the links and reading the new rss of today
"""
    a.read the single line
    b.select from that with a for cicle (or while we will see) the news of today
    c. publish them beautifully
    d. wait and refresh
    """

all_choices = {}
temp_list = file.readlines()
#choice of the feed to parse:
for i in file.readlines():
    ii = str(i)
    all_choices[ii] = temp_list[i]
    print('[',i,']', all_choices[ii])
    
print(all_choices)

    
    
def selection(the_dict):
    z = str(input('Choose your feed: '))
    final_link = the_dict[z]
    return final_link


news = feedparser.parse(selection(all_choices))
for count in news.entries:
    news.entries[count].title
    news.entries[count].description

