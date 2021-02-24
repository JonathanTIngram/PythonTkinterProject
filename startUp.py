#Jonathan Ingram
#CSE 222
#Start up screen

import tkinter as tk
from tkinter import * #import everything from tkinter
from tkinter import messagebox

import startUp
import createAccount
import login

    
#Main Window Class
class StartUpWindow:
    def __init__(self, master):
        self.master = master 
        master.minsize(width = 500, height = 350) #Setting Window size
        master.title("Rest-A-While")
        master.configure(bg="#333130")

        def checkSoldout():

            with open("File Handling/updatedRoomNums.txt", "r") as fp:
                newRoomNums = fp.read()
                newRoomNums = [int(x) for x in newRoomNums.split()]

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

                master.destroy()
                import soldout

        checkSoldout()

        def cancelButtonClicked():
            

            cancel = messagebox.askquestion("Cancel?",
                                            "Are you sure you want to cancel?")

            if (cancel == "yes"): #yes is given when the yes button is clicked
                messagebox.showinfo("Canceled",
                    "Goodbye")
                master.destroy() #closes program
            else:
                messagebox.showinfo("Return",
                                    "Canceled")

        def loginButtonClicked():

            loginButton.destroy()
            createAcctButton.destroy()
            hotelLayoutLabel.destroy()
            cancelButton.destroy()
            headerLabel.destroy()
            
            #change the window size
            master.minsize(width=400, height=250)
            

            loginW = login.LoginWindow(master)
            
            

            
        def createAcctButtonClicked():
            

            loginButton.destroy()
            createAcctButton.destroy()
            hotelLayoutLabel.destroy()
            cancelButton.destroy()
            headerLabel.destroy()
            
            #change the window size
            master.minsize(width=400, height=250)
            
            #create an instance of the createAcctWindow Class
            createA = createAccount.CreateAcctWindow(master)

            

            #if an account if sucsessfully created
            #the main window get set to its origonal
            #state but the login button is enabled


        #creating images

        hotelPhoto = PhotoImage(file = "Images/hotelOutside.png")

        hotelLayoutLabel = Label(image = hotelPhoto)

        hotelLayoutLabel.image = hotelPhoto

        hotelLayoutLabel.grid(row=3, column=3)

        #Creating Labels

        headerLabel = Label(master, text="Rest-A-While", fg="WHITE",
                            bg="#333130", font=("Courier", 20),)
        headerLabel.grid(row=1,column=3)        

        #Creating Buttons

        loginButton = Button(text="Login", fg="WHITE", bg="BLACK",
                             width=15, height=3,
                             command = loginButtonClicked,
                             activebackground="#4d231f")
        loginButton.grid(row=4, column=2, padx=25)

        cancelButton = Button(text="Cancel", fg="WHITE",
                              bg="BLACK", width=15, height=3,
                              activebackground="#4d231f",
                              command = cancelButtonClicked)
        cancelButton.grid(row=4, column=5, pady=20, padx=25)

        createAcctButton = Button(text="Create Account",
                                  fg="WHITE", bg="BLACK",
                                  width=15, height=3,
                                  activebackground="#4d231f",
                                  command = createAcctButtonClicked)
        createAcctButton.grid(row=4, column=3, padx=25)

        def config_mainWindow():

            master.minsize(width = 500, height = 350) #Setting Window size
            master.title("Rest-A-While")
            

            hotelPhoto = PhotoImage(file = "Images/hotelOutside.png")

            hotelLayoutLabel = Label(image = hotelPhoto)

            hotelLayoutLabel.image = hotelPhoto

            hotelLayoutLabel.grid(row=3, column=3)

            #Creating Labels      

            #Creating Buttons

            loginButton = Button(text="Login", fg="WHITE", bg="BLACK",
                                 width=15, height=3,
                                 activebackground="#4d231f",
                                 command = loginButtonClicked,
                                 )
            loginButton.grid(row=4, column=2, padx=25)

            cancelButton = Button(text="Cancel", fg="WHITE",
                                  bg="BLACK", width=15, height=3,
                                  activebackground="#4d231f",
                                  command = cancelButtonClicked,
                                  )
            cancelButton.grid(row=4, column=5, pady=20, padx=25)

            createAcctButton = Button(text="Create Account",
                                      fg="WHITE", bg="BLACK",
                                      width=15, height=3,
                                      activebackground="#4d231f",
                                      command = createAcctButtonClicked)
            createAcctButton.grid(row=4, column=3, padx=25)
