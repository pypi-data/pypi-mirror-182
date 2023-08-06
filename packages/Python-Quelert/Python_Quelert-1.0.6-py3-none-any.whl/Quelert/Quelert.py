from tkinter import messagebox
from datetime import datetime

import Stopwatch_ru
import Stopwatch_en

import webbrowser
import calendar
import datetime
import qrcode
import wget


class Quelert:
    Version = "v1.0.6"
    VersionCode = "V1Q6p311"
    ReleaseDate = "22.12.2022"

class QlBrowser:
    NamesLib = ["Webbrowser", "Wget"]

    def open(url):
        webbrowser.open(url)

    def download(url, pathsave):
        wget.download(url, pathsave)

class QlDateTime:
    NamesLib = ["Datetime", "Calendar"]
    Date = datetime.date.today()

    def Time():
        date_time = datetime.datetime.now()
        current = date_time.time()
        print(current)

    def Calendar(Year, Month):
        november = calendar.month(Year, Month)
        print(november)

class QlWidgets:
    NamesLib = ["Tkinter"]
    Stopwatch_Lang = ["ru", "en"]

    def ERROR(title, message):
        messagebox.showerror(title, message)

    def WARNING(title, message):
        messagebox.showwarning(title, message)

    def INFO(title, message):
        messagebox.showinfo(title, message)

    def Stopwatch(lang):
        if lang == "ru":
            Stopwatch_ru.stopwatch()

        elif lang == "en":
            Stopwatch_en.stopwatch()

    def QrCode(text, namefile):
        img = qrcode.make(text)
        img.save(namefile)