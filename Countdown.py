import tkinter as tk
import datetime
import os
class TurnOffApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.entry = tk.Entry()
        self.entry.pack()
        self.settime = tk.Button(text="Set time until shutdown", width=25, height=5, bg="blue", fg="yellow",command= self.turnitoff)
        self.extend_button = tk.Button(text="Click here to extend time",width=25,height=5,bg="blue",fg="yellow",command = self.extendtime)
        self.reduce_button = tk.Button(text="Click here to reduce time", width=25, height=5, bg="blue", fg="yellow",command=self.reducetime)
        self.settime.pack()
        self.extend_button.pack()
        self.reduce_button.pack()

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            os.system("shutdown /s /t 1")
        else:
            self.label.configure(text=str(datetime.timedelta(seconds=self.remaining)))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def turnitoff(self):
        timetosleep = float(self.entry.get())
        self.countdown(timetosleep)
    def extendtime(self):
        self.remaining += 3600
    def reducetime(self):
        self.remaining -= 1800
if __name__ == "__main__":
    app = TurnOffApp()
    app.mainloop()