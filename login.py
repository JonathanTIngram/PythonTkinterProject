#Jonathan Ingram
#CSE 222
#Create Account Window

from tkinter import * 
from tkinter import messagebox

import startUp
import floorPlan

def cUser(currentUser):
    
    currentU = currentUser

    return currentU  

class LoginWindow():

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
            
            print("username: " + userNameText)
            print("password: " + passwordText)

                    
            userfile = open("File Handling/userNames.txt", "r") #writes to username file
            userList = userfile.readlines()

            passwordFile = open("File Handling/passwords.txt", "r")
            passwordList = passwordFile.readlines()
            

            sizeofUList = len(userList)
            sizeofPList = len(passwordList)

            UNfound = False #to see if a username was found
            PWfound = False #to see if a password was found
            i = 0 #initalize i 
            
            while (i < sizeofUList): #acts like a c++ for loop
                if(userList[i] == userNameText + "\n"):
                    print("username is " + userList[i])
                    UNfound = True #username was found
                else:
                    print("no username: " + userList[i])
                    
                    
                if(passwordList[i] == passwordText + "\n"):
                    print("password is: " + passwordList[i])
                    PWfound = True
                else:
                    print("no password: " + passwordList[i])

                i += 1

            if(PWfound == True and UNfound == True):

                validUN = messagebox.showinfo("Login",
                                                  "You logged in")
                
                    
               #morph window to setup for instance of Floor_Plan_Window()
                userNameLabel.destroy()
                userNameTextbox.destroy()

                passwordLabel.destroy()
                passwordTextbox.destroy()

                submitButton.destroy()


                currentUser = open("File Handling/currentUser.txt", "w") #writes to username file
                currentUser.writelines(userNameText)

                currentUser.close()
  
                fPlanWindow = floorPlan.Floor_Plan_Window(master)
                print("Instance of Floor_Plan_Winodw class from floorPlan.py")
                

            if(UNfound == False):
                print("invalid user")
                invaidUN = messagebox.showinfo("Login",
                                               "Username already exists")
            if(PWfound == False):
                print("invalid password")
                invalidPW = messagebox.showinfo("Login", "Invalid Password")

                
            
                
            def return_to_main():
                master.destroy()
            

        #end of submitButtonClicked
 

        #End of sumbitButtonClicked method
        #creating labels

        userNameLabel = Label(master, text = "Enter your username",
                              font=("Courier", 20), fg="WHITE",
                               bg="#333130")
        userNameLabel.grid(row=2,column=3,
                           padx=65, pady=10)

        passwordLabel = Label(master, text = "Enter your password",
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
                              fg="WHITE", bg="BLACK",
                              width=15, height=3,
                              activebackground="#4d231f",
                              command = submitButtonClicked) #when defining command you have to call a function
                                                                                                               #without ()
        submitButton.grid(row=6, column=3, pady=40)

        passwordTextbox.bind('<Return>', submitButtonClicked)

        cancelButton = Button(text="Cancel", fg="WHITE",
                              bg="BLACK", width=15, height=3,
                              activebackground="#4d231f",
                              command = cancelButtonClicked)
        cancelButton.grid(row=7, column=3)

        headerLabel = Label(master, text="Rest-A-While", fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        headerLabel.grid(row=1,column=3) 

    

#End of LoginWindow Class
