from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from PIL import Image

import Stopwatch_ru
import Stopwatch_en
import Timer

import webbrowser
import datetime
import calendar
import qrcode
import wget
import rich
import time
import os

class Quelert:
    Version = "2.0.1"

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

    def OpenDirectory():
        filedialog.askdirectory()

    def OpenNameFile():
        filedialog.askopenfilename()

    def Stopwatch(lang):
        if lang == "ru":
            Stopwatch_ru.stopwatch()

        elif lang == "en":
            Stopwatch_en.stopwatch()

    def Timer(lang):
        if lang == "ru":
            Timer.ru()

        elif lang == "en":
            Timer.en()

    def QrCode(text, namefile):
        img = qrcode.make(text)
        img.save(namefile)

    def ColorMania():
        os.system("CM\\ColorMania.exe")