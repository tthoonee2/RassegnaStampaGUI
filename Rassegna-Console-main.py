import requests
import feedparser
####THE CODE IS STRUCTURED AS FOLLOWS:
#1. Import and save custom feed links
"""
    a. input of link
    b. request of link - verify get and try exception [200]
    c.add link to a new line in the file.
"""
file = open('linkssaved.txt', 'x')
choice = input('insert a link? [y/n]\n')
if choice is y:
    while choice is 'y':
        new_link = str(input('insert a new link to be added to your favorites: '))
        try:
            response = requests.get(new_link)
            if response == 200: #loaded the rss, so the link is very much probably valid
                file = open("linkssaved.txt", "w")
                file.write(new_link,'\n')
                choice = input('insert a link? [y/n]\n')
        except:
                print('unable to open the file')
                break

    #run the rest of the program
try:
    file = open.file("linksaved.txt", 'rt')
except:
    print('unable to open the file')

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
    

def selection(the_dict):
    z = str(input('Choose your feed: '))
    final_link = the_dict[z]
    return final_link

news = feedparser.parse(selection(all_choices))
for count in news.entries:
    news.entries[count].title
    news.entries[count].description

