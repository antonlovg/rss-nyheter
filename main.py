import feedparser
import tkinter as tk

# Skapar huvudfönstret
huvuddel = tk.Tk()
huvuddel.title("RSS Läsare")

# Skapar listbox
listbox = tk.Listbox(huvuddel)
listbox.pack()

# Skapar widget för att visa artiklar
artikel_text = tk.Text(huvuddel)
artikel_text.pack()


# Funktion för att visa vald artikel
def visa_artikel(handelse):
    vald_index = listbox.curselection()[0]
    vald_link = links[vald_index]

    artikel = feedparser.parse(vald_link)
    artikel_text.delete(1.0, tk.END)
    artikel_text.insert(tk.END, artikel.entries[0].description)


# Lägger till en händelse för att visa artiklar när en rubrik väljs
listbox.bind("<<ListboxSelect>>", visa_artikel)

############################

rss_url = "https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/"
feed = feedparser.parse(rss_url)

# Hämtar rubriker och länkar
rubriker = [entry.title for entry in feed.entries]
links = [entry.links for entry in feed.entries]

# Fyller listbox med rubriker
for rubrik in rubriker:
    listbox.insert(tk.END, rubrik)


# Startar GUI
huvuddel.mainloop()