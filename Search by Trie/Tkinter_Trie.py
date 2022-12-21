from tkinter import *
import Trie_2

root = Tk()
root.geometry("500x300")


def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)


def fillout(e):
    # Delete whatever is in the entry box
    my_entry.delete(0, END)

    # Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))


def check(e):
    # grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = trie.search("")
    else:
        data = trie.search(typed)

    # update our listbox with selected items
    update(data)


my_label = Label(root, text="Start Typing...",
                 font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

trie = Trie_2.Trie()
list_insert = ["appData", "appData", "application Data", "bash_history", "contacts", "cookies",
               "creative Cloud Files", "docker", "desktop", "documents", "downloads", "favorites", "gitconfig",
               "idlerc", "ipython", "idlerc", "jupyter", "java", "lesshst", "links", "local Settings",
               "netHood", "matplotlib", "music", "recent", "templates"]
for string in list_insert:
    trie.insert(string)
toppings = trie.search("")
update(toppings)

my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>", check)

root.mainloop()
