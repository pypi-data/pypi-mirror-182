from tkinter import *
from tkinter import ttk
from datetime import datetime

temp = 0
after_id = ''

def stopwatch():
    root = Tk()
    root.title("Stopwatch")
    root.config(bg="#222")
    root.geometry("400x200")
    root.resizable(False, False)

    def tick():
        global temp, after_id
        after_id = root.after(1000, tick)
        f_temp = datetime.fromtimestamp(temp).strftime("%W:%M:%S")
        Sw.configure(text=str(f_temp))
        temp += 1

    def Start():
        btnStart.place_forget()
        btnStop.place(relx=0.5, rely=0.5, anchor=CENTER)
        tick()

    def Stop():
        btnStop.place_forget()
        btnContinue.place(x=115, y=5)
        btnReset.place(x=205, y=5)
        root.after_cancel(after_id)

    def Reset():
        global temp
        temp = 0
        Sw.configure(text="00:00:00")
        btnContinue.place_forget()
        btnReset.place_forget()
        btnStart.place(relx=0.5, rely=0.5, anchor=CENTER)

    def Continue():
        btnContinue.place_forget()
        btnReset.place_forget()
        btnStop.place(relx=0.5, rely=0.5, anchor=CENTER)
        tick()

    Sw = Label(root, text="00:00:00", bg="#222", fg="white", font="Consolas 40 bold")
    Sw.place(relx=0.5, rely=0.4, anchor=CENTER)

    Control = Frame(root, bg="#363636", height=35)
    Control.pack(fill=BOTH, side=BOTTOM)

    btnStart = ttk.Button(Control, text="Start", command=Start)
    btnStop = ttk.Button(Control, text="Stop", command=Stop)
    btnReset = ttk.Button(Control, text="Reset", command=Reset)
    btnContinue = ttk.Button(Control, text="Continue", command=Continue)

    btnStart.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    stopwatch()
