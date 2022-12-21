import Trie

object_File = Trie
object_Trie = object_File.Trie()


def Insert():
    list_insert = ["appData", "appData", "application Data", "bash_history", "contacts", "cookies",
                   "Creative Cloud Files", "docker", "desktop", "documents", "downloads", "favorites", "gitconfig",
                   "idlerc", "ipython", "idlerc", "jupyter", "java", "lesshst", "Links", "Local Settings",
                   "NetHood", "matplotlib", "Music", "recent", "templates"]
    for string in list_insert:
        object_Trie.insert(string)
    input_ = input("Enter : ")
    object_Trie.insert(input_)
