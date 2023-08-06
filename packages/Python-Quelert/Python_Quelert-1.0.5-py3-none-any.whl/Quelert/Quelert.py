from tkinter import messagebox

import webbrowser
import calendar
import datetime
import wget


class Quelert:
    Version = "v1.0.5"
    CodeVersion = "F1Q5a"
    ReleaseDate = "20.12.2022"

class Browser:
    NamesLib = "Webbrowser\nWget"

    def open(self, url):
        webbrowser.open(url)

    def download(self, url, pathsave):
        wget.download(url, pathsave)

class DateTime:
    NamesLib = "Calendar\nDatetime"
    Date = datetime.date.today()

    def Time(self):
        date_time = datetime.datetime.now()
        current = date_time.time()
        print(current)

    def Calendar(self, Year, Month):
        november = calendar.month(Year, Month)
        print(november)

class Widgets:
    NamesLib = "Tkinter"

    def ERROR(self, title, message):
        messagebox.showerror(title, message)

    def WARNING(self, title, message):
        messagebox.showwarning(title, message)

    def INFO(self, title, message):
        messagebox.showinfo(title, message)