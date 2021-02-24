#Jonathan Ingram
#CSE 222
#Create Account Window

from tkinter import * 
import tkinter
from tkinter import messagebox

import startUp



class CreateAcctWindow():
    def __init__(self, master):
        #main window of create account window

        def return_to_main():
            userNameLabel.destroy()
            passwordLabel.destroy()
            userNameTextbox.destroy()
            passwordTextbox.destroy()
            submitButton.destroy()
            cancelButton.destroy()
            headerLabel.destroy()

            start = startUp.StartUpWindow(master)

        def cancelButtonClicked():

            cancel = messagebox.askquestion("Cancel?",
                                            "Would you like to leave completly?")

            if (cancel == "yes"): #yes is given when the yes button is clicked
                messagebox.showinfo("Canceled",
                    "Goodbye")
                master.destroy() #closes program
            else:
                messagebox.showinfo("Return",
                                    "You will now return to the login screen")
                return_to_main()

        def submitButtonClicked(*args):

            userNameText = userNameTextb.get()
            passwordText = passwordTextb.get()
            
            def get_username():

                file = open("File Handling/userNames.txt", "r")
                userList = file.readlines()

                i = 0
                sizeofList = len(userList) 
                while (i < sizeofList):
                    if(userList[i] == userNameText + "\n"):
                        invalidUN = messagebox.showinfo("username taken",
                                                        "The username you entered already exists")
                    i += 1

                    
                userName = open("File Handling/userNames.txt", "a") #writes to username file
                userName.writelines(userNameText + "\n")

                userName.close()


            def get_password():

                SpecialSym = ["$", "@", "#", "%", "*"]
                val = True

                if (len(passwordText) < 8):
                    print("Password should be at least eight characters long")
                    val = False
                    messagebox.showinfo("password",
                    "The password should be at least eight characters long")

                elif not any(char.isdigit() for char in passwordText):
                    print("Password should have at least one numeral")
                    val = False
                    messagebox.showinfo("password",
                    "The password should have a least one numeral")

                elif not any(char.isupper() for char in passwordText):
                    print("Password needs at least one uppercase letter")
                    val = False
                    messagebox.showinfo("password",
                    "The password should have at least one uppercase letter")

                elif not any(char.islower() for char in passwordText):
                    print("Password should have at least one lowercase letter")
                    val = False
                    messagebox.showinfo("password",
                    "The password should have at least one lowercase letter")

                elif not any(char in SpecialSym for char in passwordText):
                    print("Password should have at least one special character")
                    val = False
                    messagebox.showinfo("password",
                    "The password should have at least one special character")

                if(val):
                    print("username: " + userNameText)
                    print ("password: " + passwordText)
                    password = open("File Handling/passwords.txt", "a") #wrties to password file
                    password.writelines(passwordText + "\n")
                    print("password stored")
                    val = False



                    

                        
                        
                    get_username() #only stores username if there is a valid password

                    password.close()

                    return_to_main()

                
                else:
                    invalidPW = messagebox.showinfo("Invalid Password",
                                                    "The password you entered is invalid")

        

            get_password()

        #end of submitButtonClicked

 

        #End of sumbitButtonClicked method
        #creating labels

        userNameLabel = Label(master, text = "Create a username",
                              font=("Courier", 20), fg="WHITE",
                               bg="#333130")
        userNameLabel.grid(row=2,column=3,
                           padx=65, pady=10)

        passwordLabel = Label(master, text = "Create a password",
                              font=("Courier", 20), fg="WHITE",
                               bg="#333130")
        passwordLabel.grid(row=4, column=3, padx=65, pady=10)
        
        #creating textboxes
        userNameTextb = StringVar() #string variable for tkinter
        passwordTextb = StringVar() #in order to recieve data from the textboxes

        userNameTextbox = Entry(master, textvariable=userNameTextb) #Defining the username textbox
        userNameTextbox.grid(row=3, column=3, padx=65)

        passwordTextbox = Entry(master, textvariable=passwordTextb, show="*") #Defining the password textbox
        passwordTextbox.grid(row=5, column=3, padx=65, pady=10)

                #creating buttons
        submitButton = Button(master, text = "Submit",
                              fg="WHITE", bg="#FFFFFF",
                              width=15, height=3,
                              activebackground="#4d231f",
                              command = submitButtonClicked) #when defining command you have to call a function
                                                                                                               #without ()
        submitButton.grid(row=6, column=3, pady=40)

        passwordTextbox.bind('<Return>', submitButtonClicked)


        headerLabel = Label(master, text="Rest-A-While", fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        headerLabel.grid(row=1,column=3) 

        cancelButton = Button(text="Cancel", fg="WHITE",
                              bg="BLACK", width=15, height=3,
                              activebackground="#4d231f",
                              command = cancelButtonClicked)
        cancelButton.grid(row=7, column=3)

        

#End of CreateAcctWindow Class
