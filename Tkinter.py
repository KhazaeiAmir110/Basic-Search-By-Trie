'''
from tkinter import *
import Trie_2

root = Tk()
root.title("Auto Select")
# root.iconbitmap('c')
# root.geometry('500*300')

my_label = Label(root, text='Start typing...', font=('Helvetica', 14), fg='grey')

my_label.pack(pady=20)

my_entry = Entry(root, font=('Helvetica', 20))

my_entry.pack()

my_list = Listbox(root, width=50)
my_list.pack(pady=40)

list_insert = ["appData", "appData", "application Data", "bash_history", "contacts", "cookies",
               "Creative Cloud Files", "docker", "desktop", "documents", "downloads",
               "favorites", "gitconfig", "Links", "Local Settings", "java",
               "idlerc", "ipython", "idlerc", "jupyter", "lesshst",
               "NetHood", "matplotlib", "Music", "recent", "templates"]

object_File = Trie_2
object_Trie = object_File.Trie()


def Insert():
    list_insert = ["appData", "appData", "application Data", "bash_history", "contacts", "cookies",
                   "Creative Cloud Files", "docker", "desktop", "documents", "downloads", "favorites", "gitconfig",
                   "idlerc", "ipython", "idlerc", "jupyter", "java", "lesshst", "Links", "Local Settings",
                   "NetHood", "matplotlib", "Music", "recent", "templates"]
    for string in list_insert:
        object_Trie.insert(string)


def update(data):
    my_list.delete(0, END)
    for item in data:
        my_list.insert(END, item)


def fallout(e):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ACTIVE))


def check(e):
    typed = my_entry.get()
    if typed == '':
        data = object_Trie.output
    else:
        data = []
        for item in object_Trie.output:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)


update(list_insert)

my_list.bind("<<ListboxSelect>>", fallout)

my_entry.bind("<KeyRelease>", check)
root.mainloop()
'''

from tkinter import *

root = Tk()
# root.title('Codemy.com - Auto Select/Search')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")


# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)


# Update entry box with listbox clicked
def fillout(e):
    # Delete whatever is in the entry box
    my_entry.delete(0, END)

    # Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))


# Create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    # update our listbox with selected items
    update(data)


# Create a label
my_label = Label(root, text="Start Typing...",
                 font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
            "Cheese", "Onions", "Ham", "Taco"]

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
