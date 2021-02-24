#Jonathan Ingram
#CSE 222


from tkinter import *
import time


class SoldoutWindow:
    def __init__(self, master):
        self.master = master 
        master.minsize(width = 500, height = 350) #Setting Window size
        master.title("Rest-A-While")
        master.configure(bg="#333130")

        headerLabel = Label(master, text="All rooms are currently sold out,\n please check back another\n time for a reservation", fg="WHITE",
                            bg="#333130", font=("Courier", 20),pady=100)
        headerLabel.grid(row=1,column=2)

        soldOutLabel = Label(master, text="Thank you for choosing Rest-A-While hotel services", fg="WHITE",
                            bg="#333130", font=("Courier", 20),pady=200)
        soldOutLabel.grid(row=2,column=2)

        

root = Tk()
receiptWin = SoldoutWindow(root)
root.mainloop()
