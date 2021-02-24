#Jonathan Ingram
#CSE 222
#Manager Output Window
#The manager would run this program in order to see
#which rooms are reserved 

from tkinter import * #import everything from tkinter
from tkinter import messagebox

import startUp





class Manager_Output_Window():
    
    def __init__(self, master):

        self.master = master
        master.minsize(width = 700, height = 350) #Setting Window size
        master.title("Rest-A-While")
        master.configure(bg="#333130")

        with open("File Handling/updatedRoomNums.txt", "r") as fp:
            newRoomNums = fp.read()
            newRoomNums = [int(x) for x in newRoomNums.split()]

        

        print(newRoomNums)

        with open("File Handling/totalPrice.txt", "r") as fp:
            totalPrice = fp.read()
        fp.close()


        if(newRoomNums[0] == 0\
            and newRoomNums[1] == 0\
            and newRoomNums[2] == 0\
            and newRoomNums[3] == 0\
            and newRoomNums[4] == 0\
            and newRoomNums[5] == 0\
            and newRoomNums[6] == 0\
            and newRoomNums[7] == 0\
            and newRoomNums[8] == 0\
            and newRoomNums[9] == 0\
            and newRoomNums[10] == 0\
            and newRoomNums[11] == 0\
            and newRoomNums[12] == 0\
            and newRoomNums[13] == 0\
            and newRoomNums[14] == 0):

            messagebox.showinfo("All out",
                    "All rooms are reserved")

            

        def floorSelected(*args):

            floors = floorOption_var.get()

            if(floors == "Floor 1"):
                KingRoomA.configure(text=newRoomNums[0])
                KingRoomR.configure(text=str(4 - newRoomNums[0]))

                TwinRoomA.configure(text=newRoomNums[3])
                TwinRoomR.configure(text=str(2 - newRoomNums[3]))

                DeluxeKingRoomA.configure(text=newRoomNums[6])
                DeluxeKingRoomR.configure(text=str(4 - newRoomNums[6]))

                CornerKingRoomA.configure(text=newRoomNums[9])
                CornerKingRoomR.configure(text=str(4 - newRoomNums[9]))

                CornerSuiteA.configure(text=newRoomNums[12])
                CornerSuiteR.configure(text=str(2 - newRoomNums[12]))
            
            elif(floors == "Floor 2"):
                KingRoomA.configure(text=newRoomNums[1])
                KingRoomR.configure(text=str(4 - newRoomNums[1]))

                TwinRoomA.configure(text=newRoomNums[4])
                TwinRoomR.configure(text=str(2 - newRoomNums[4]))

                DeluxeKingRoomA.configure(text=newRoomNums[7])
                DeluxeKingRoomR.configure(text=str(4 - newRoomNums[7]))

                CornerKingRoomA.configure(text=newRoomNums[10])
                CornerKingRoomR.configure(text=str(4 - newRoomNums[10]))

                CornerSuiteA.configure(text=newRoomNums[13])
                CornerSuiteR.configure(text=str(2 - newRoomNums[13]))  

            elif(floors == "Floor 3"):
                KingRoomA.configure(text=newRoomNums[2])
                KingRoomR.configure(text=str(4 - newRoomNums[2]))

                TwinRoomA.configure(text=newRoomNums[5])
                TwinRoomR.configure(text=str(2 - newRoomNums[5]))

                DeluxeKingRoomA.configure(text=newRoomNums[8])
                DeluxeKingRoomR.configure(text=str(4 - newRoomNums[8]))

                CornerKingRoomA.configure(text=newRoomNums[11])
                CornerKingRoomR.configure(text=str(4 - newRoomNums[11]))

                CornerSuiteA.configure(text=newRoomNums[14])
                CornerSuiteR.configure(text=str(2 - newRoomNums[14]))          
   
                

        #Headers for room types

        KingRoomH = Label(master, text = "King Rooms:",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        KingRoomH.grid(row=2, column=1)

        TwinRoomH = Label(master, text = "Twin Rooms:",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        TwinRoomH.grid(row=3, column=1)

        DeluxeKingRoomH = Label(master, text = "Deluxe King Rooms:",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        DeluxeKingRoomH.grid(row=4, column=1)

        CornerKingRoomH = Label(master, text = "Corner King Rooms:",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerKingRoomH.grid(row=5, column=1)

        CornerSuiteH = Label(master, text = "Corner Suites:",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerSuiteH.grid(row=6, column=1)

        #Rooms Available
        RoomsA = Label(master, text = "Available",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        RoomsA.grid(row=1, column=2)

        KingRoomA = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        KingRoomA.grid(row=2, column=2)

        TwinRoomA = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        TwinRoomA.grid(row=3, column=2)

        DeluxeKingRoomA = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        DeluxeKingRoomA.grid(row=4, column=2)

        CornerKingRoomA = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerKingRoomA.grid(row=5, column=2)

        CornerSuiteA = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerSuiteA.grid(row=6, column=2)

        #Rooms Reserved
        RoomsR = Label(master, text = "   Reserved",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        RoomsR.grid(row=1, column=3)

        KingRoomR = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        KingRoomR.grid(row=2, column=3)

        TwinRoomR = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        TwinRoomR.grid(row=3, column=3)

        DeluxeKingRoomR = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        DeluxeKingRoomR.grid(row=4, column=3)

        CornerKingRoomR = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerKingRoomR.grid(row=5, column=3)

        CornerSuiteR = Label(master, text = "-",
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        CornerSuiteR.grid(row=6, column=3)


        floorOptionList = ("Floor 1", "Floor 2", "Floor 3")

        floorOption_var = StringVar()

        floorOption_var.set("Floor Selection") #set to the fisrt value in the drop down menu
        
        floorOption_menu = OptionMenu(master, floorOption_var, *floorOptionList, command=floorSelected)
        floorOption_menu.grid(row = 7, column = 1, sticky="W")
        floorOption_menu.configure(bg="BLACK", fg="WHITE",
                              width = 15, height = 2,
                              bd=3, #items within the menu's width
                              activebackground="#4d231f")

        revenueLabel = Label(master, text ="Total Revenue: $" + str(totalPrice),
                        font=("Courier", 20), fg="WHITE",
                        bg="#333130")

        revenueLabel.grid(row=7, column=2)

        def cancelButtonClicked():
    
            cancel = messagebox.askquestion("Cancel?",
                                            "Are you sure you want to cancel?")

            if (cancel == "yes"): #yes is given when the yes button is clicked
                messagebox.showinfo("Canceled",
                                    "Goodbye")
                master.destroy()
            else:
                messagebox.showinfo("Return",
                                    "You will now return")


        cancelButton = Button(master, text="Cancel",
                            bg="BLACK", fg="WHITE",
                            width=15, height=3,
                            activebackground="#4d231f",
                            command=cancelButtonClicked)
        cancelButton.grid(row=7, column=3)



root = Tk()
Manager_Output_Window(root)
root.mainloop()
