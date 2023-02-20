import webbrowser
import sys
import pyperclip

sys.argv

if len(sys.argv) > 1:
    #["webscraper.py", "870", "Valencia", "St."] "870 Valencia St."
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()
    

    
webbrowser.open("https://www.google.com/maps/place/" + address)