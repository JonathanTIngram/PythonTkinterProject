#Jonathan Ingram 
#CSE 222
#Receipt display

from tkinter import *
import datetime
from datetime import date

class ReceiptWindow:
    def __init__(self, master):
        self.master = master 
        master.minsize(width = 500, height = 350) #Setting Window size
        master.title("Rest-A-While")
        master.configure(bg="#333130")



        f = open("File Handling/currentUser.txt", "r") #writes to username file
        currentUser = f.readlines()
        f.close()

        with open("File Handling/currentPrice.txt", "r") as fp:
            currentPrice = fp.read()
        fp.close()

        headerLabel = Label(master, text="          Rest-A-While", fg="WHITE",
                            bg="#333130", font=("Courier", 20),)
        headerLabel.grid(row=1,column=1)  

        costumerLabel = Label(master, text="User confirmation: ", fg="WHITE",
                            bg="#333130", font=("Courier", 20),)
        costumerLabel.grid(row=2,column=1,sticky=W)

        costumerNameLabel = Label(master, text=currentUser, fg="WHITE",
                            bg="#333130", font=("Courier", 20),)
        costumerNameLabel.grid(row=2,column=2) 

        priceLabel = Label(master, text="Price:", fg="WHITE",
                            bg="#333130", font=("Courier", 20),)
        priceLabel.grid(row=3,column=1,sticky=W)

        customerPriceLabel = Label(master, text="$" + currentPrice, fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        customerPriceLabel.grid(row=3,column=2)

        dateLabel = Label(master, text="Reservation made on:", fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        dateLabel.grid(row=4,column=1,sticky=W)

        dateLabel = Label(master, text=str(date.today()), fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        dateLabel.grid(row=4,column=2)


        thanksLabel = Label(master, text="          Thank you for choosing\n          Rest-A-While hotel servies", fg="WHITE",
                            bg="#333130", font=("Courier", 20),pady=50)
        thanksLabel.grid(row=5,column=1)

        



root = Tk()
receiptWin = ReceiptWindow(root)
root.mainloop()
