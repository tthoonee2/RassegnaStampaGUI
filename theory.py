import tkinter as tk


#to create a new window
window = tk.Tk()
#to add a widget
#greeting = tk.Label(text='hello world')
#greeting.pack()
#with window.mainloop() python listens for events
#window.mainloop() #where mainloop is the method for listening to new events
#the following are all types of widgets
#label
#button
#entry
#text
#frame

#Useful label:
label = tk.Label(
    text='Label_txt',
    fg="blue", #can be hexadecimal
    bg='green', #can be hexadecimal
    width=50,
)

#getting user imput
#.get() , .delete() it deletes the text, .insert() inserts the text
entry = tk.Entry(
fg = 'yellow',
bg= 'blue',
width = 50

)
#entry get a oneline user input

entry.pack()
name = entry.get()
window.mainloop()
name

#useful button
button = tk.Button(
    text='Click me',
    fg='white',
    bg='blue'

)