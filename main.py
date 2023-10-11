########################################################
# Gjord av Anton Lövgren
# v0.1.1 - Hämtar RSS-flöden från olika svenska hemsidor
# Nytt i v0.1.1:
# Ifall ingen artikel finns så blir det ett felmeddelande
# Utökat bredden på rubriker
########################################################
# Att göra:
# * Välja ämne (tex sport, nyheter, ekonomi)
# * Länkar till hemsidor
# * Snygga till utseendet
########################################################

import feedparser
import tkinter as tk
from datetime import datetime

# Skapa huvudfönstret
huvuddel = tk.Tk()
huvuddel.title("RSS Läsare")

# Skapa listbox
listbox = tk.Listbox(huvuddel, width=100)
listbox.pack()

# Skapa Text-widget för att visa artiklar
artikel_text = tk.Text(huvuddel)
artikel_text.pack()


# Funktion för att visa vald artikel
def visa_artikel(event):
    vald_index = listbox.curselection()
    if vald_index:  # Kontrollera om en rad är vald
        vald_index = vald_index[0]
        vald_link = links[vald_index]

        artikel = feedparser.parse(vald_link)
        artikel_text.delete(1.0, tk.END)
        if artikel.entries:
            artikel_text.insert(tk.END, format_artikel(artikel))
        else:
            artikel_text.insert(tk.END, "Ingen artikel tillgänglig.")


# Lägg till en händelse för att visa artiklar när en rubrik väljs
listbox.bind("<<ListboxSelect>>", visa_artikel)


# Funktion för att formatera artiklar enligt önskat format
def format_artikel(artikel):
    rubrik = artikel.entries[0].title
    beskrivning = artikel.entries[0].description
    publicerings_tid = datetime.strptime(artikel.entries[0].published, '%a, %d %b %Y %H:%M:%S %z')
    kalla = artikel.feed.title

    formaterad_artikel = f"*{rubrik}*\n{beskrivning}\nHämtad från: {kalla}\nPublicerad tid: {publicerings_tid}\n\n"

    return formaterad_artikel


# Lista över RSS-källor
rss_kallor = [
    "https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/",
    "https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/sport/",
    "https://rss.aftonbladet.se/rss2/small/pages/sections/sportbladet/fotboll/"
    # Lägg till fler RSS-källor här
]

# Hämta rubriker och länkar från alla RSS-källor
rubriker = []
links = []

for rss_url in rss_kallor:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        rubriker.append(entry.title)
        links.append(entry.link)

# Fyll listbox med rubriker
for rubrik in rubriker:
    listbox.insert(tk.END, rubrik)

# Starta GUI
huvuddel.mainloop()
