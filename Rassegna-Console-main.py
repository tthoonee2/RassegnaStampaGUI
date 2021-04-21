import requests
import feed
####THE CODE IS STRUCTURED AS FOLLOWS:
#1. Import and save custom feed links
"""
    a. input of link
    b. request of link - verify get and try exception [200]
    c.add link to a new line in the file.
"""

choice = input('insert a link? [y/n]\n')
if choice is 'y':
    new_link = str(input('insert a new link to be added to your favorites: '))
    response = requests.get(new_link)
    if response == 200: #loaded the rss, so the link is very much probably valid
        try:
            file = open("linkssaved.txt", "w")
            file.write(new_link,'\n')
        except:
            print('unable to open the file')
else:
    #run the rest of the program
    try:
        file = open.file("linksaved.txt", 'r')
    except:
        print('unable to open the file')

#2.access the links and reading the new rss of today
"""
    a.read the single line
    b.select from that with a for cicle (or while we will see) the news of today
    c. publish them beautifully
    d. wait and refresh
    """
    
file.readline

    
