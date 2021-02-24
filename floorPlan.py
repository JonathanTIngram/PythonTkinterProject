#Jonathan Ingram
#CSE 222
#Floor Plans
#User will be prompted with two option lists to decide which room they will be reserving
#the purchase button is then only enabled when all three option menus are filled
#with the users room selection  



from tkinter import *
from tkinter import messagebox

import os

import startUp

import login #to get the current user

import reciept


#Floor Plan window Class 

class Floor_Plan_Window():

    def __init__(self, master):
          

        self.master = master
        master.minsize(width = 500, height = 350) #Setting Window size
        master.title("Rest-A-While")
        master.configure(bg="#333130")

        hotelPhoto = PhotoImage(file = "Images/hotelLayout.png")

        hotelLayoutLabel = Label(image = hotelPhoto)

        hotelLayoutLabel.image = hotelPhoto

        hotelLayoutLabel.grid(row=1, column=2)

        #check if a room is alredy reserved here so that the option doesnt show

      
        def showReceipt():
              startUp.StartUpWindow.__init__.cancelButton.destroy()
             

        def purchaseRoomSelection(*args):

            #get the values from each of the
            #drop down menus when submit button is clicked
             room = roomOption_var.get()
             floor = floorOption_var.get()

            #print selctions to consle
             print("Floor: " + floor)
             print("Room: " + room)
             
            #store the price for every room sold
             
        
            
           
      

             soldOut = False

             currentPrice = 0

             if(soldOut == False):
                  
                  print("Reservation Made")


                  #Varables for stroring how many of each type of room
                  #stored in NumOfRoomsReserved.xls


                  #store values from excel file on to variables

                  #Number of rooms for each room type on each floor
                  floor1KingRooms = 4
                  floor2KingRooms = 4
                  floor3KingRooms = 4

                  floor1TwinRooms = 2
                  floor2TwinRooms = 2
                  floor3TwinRooms = 2

                  floor1DKingRooms = 4
                  floor2DKingRooms = 4
                  floor3DKingRooms = 4

                  floor1CornerKingRooms = 4
                  floor2CornerKingRooms = 4
                  floor3CornerKingRooms = 4

                  floor1CornerSuites = 2
                  floor2CornerSuites = 2
                  floor3CornerSuites = 2

                  isRoomBought = False #bool is set false until at least

                  startRoomNums = [4, 4, 4,
                  2, 2, 2,
                  4, 4, 4,
                  4, 4, 4,
                  2, 2, 2]

                  noF1KingRooms = False
                  noF2KingRooms = False
                  noF3KingRooms = False

                  noF1TwinRooms = False
                  noF2TwinRooms = False
                  noF3TwinRooms = False

                  noF1DeluxeKingRooms = False
                  noF2DeluxeKingRooms = False
                  noF3DeluxeKingRooms = False

                  noF1CornerKingRooms = False
                  noF2CornerKingRooms = False
                  noF3CornerKingRooms = False

                  noF1CornerSuites = False
                  noF2CornerSuites = False
                  noF3CornerSuites = False

                  #List to put in file
                  with open("File Handling/startRoomNums.txt", "r") as f:
                        startRoomNums = f.read()
                  f.close()
                  print("Starting room amounts:")
                  print(startRoomNums)

                  #if no rooms have been rerserved load the origonal list of rooms
                  with open("File Handling/updatedRoomNums.txt", "r") as fp:
                        newRoomNums = fp.read()
                        newRoomNums = [int(x) for x in newRoomNums.split()]
                  fp.close()
                  print("updated Room nums before procedure:")
                  print(newRoomNums)

                               
                              
                  



                  floorAroom = floor + " " + room
                  roomIsReserved = False

                  if(floorAroom == "Floor 1 King Room"):
                        
                        if(newRoomNums[0] != 0):
                              print("King Room purchased")
                              newRoomNums[0] = newRoomNums[0] - 1
                              roomIsReserved = True
                              print(newRoomNums[0])
                              currentPrice = 59

                        elif (newRoomNums[0] <= 0):
                              print("No more King Rooms on floor 1")
                              noF1KingRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more King Rooms available on floor 1")


                  elif(floorAroom == "Floor 2 King Room"):

                        if(newRoomNums[1] != 0):
                              newRoomNums[1] = newRoomNums[1] - 1
                              roomIsReserved = True
                              print(floor2KingRooms)
                              currentPrice = 59

                        elif (newRoomNums[1] <= 0):
                              print("No more King Rooms on floor 2")
                              noF2KingRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more King Rooms available on floor 2")

                  elif(floorAroom == "Floor 3 King Room"):
                        
                        if(newRoomNums[2] != 0):
                              newRoomNums[2] = newRoomNums[2] - 1
                              print(floor3KingRooms)
                              roomIsReserved = True
                              currentPrice = 59

                        elif(newRoomNums[2] <= 0):
                              print("No more King Rooms on floor 3")
                              noF3KingRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more King Rooms available on floor 3")
                  #Twin Room
                  elif(floorAroom == "Floor 1 Twin Room"):
                        
                        if(newRoomNums[3] != 0):
                              newRoomNums[3] = newRoomNums[3] - 1
                              roomIsReserved = True
                              print(floor1TwinRooms)
                              currentPrice = 69
                   

                        elif(newRoomNums[3] <= 0):
                              print(("No more twin rooms on Floor 1"))
                              noF1TwinRooms = True                           
                              messagebox.showinfo("Room Taken",
                              "There are no more Twin Rooms available on floor 1")    
                              
                  elif(floorAroom == "Floor 2 Twin Room"):
                        
                        if(newRoomNums[4] != 0):
                              newRoomNums[4] = newRoomNums[4] - 1
                              roomIsReserved = True
                              print(floor2TwinRooms)
                              currentPrice = 69

                        elif (newRoomNums[4] <= 0):
                              print("No more Twin Rooms on Floor 2")
                              noF2TwinRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Twin Rooms available on floor 2")   

                              
                  elif(floorAroom == "Floor 3 Twin Room"):

                        if(newRoomNums[5] != 0) :
                              newRoomNums[5] = newRoomNums[5] - 1
                              roomIsReserved = True
                              print(floor3TwinRooms)
                              currentPrice = 69

                        elif (newRoomNums[5] <= 0):
                              print("No more Twin Rooms on floor 3")
                              noF3TwinRooms = True  
                              messagebox.showinfo("Room Taken",
                              "There are no more Twin Rooms available on floor 3")   
                  #Deluxe King Room
                  elif(floorAroom == "Floor 1 Deluxe King Room"):
                        
                        if(newRoomNums[6] != 0):
                              newRoomNums[6] = newRoomNums[6] - 1
                              roomIsReserved = True
                              print(floor1DKingRooms)
                              currentPrice = 75

                        elif (newRoomNums[6] <= 0):
                              print("No more Deluxe King Rooms on Floor 1")
                              noF1DeluxeKingRooms = True 
                              messagebox.showinfo("Room Taken",
                              "There are no more Deluxe King Rooms available on floor 1")   
                  elif(floorAroom == "Floor 2 Deluxe King Room"):

                        if(newRoomNums[7] != 0):
                              newRoomNums[7] = newRoomNums[7] - 1
                              roomIsReserved = True
                              print(floor2DKingRooms)
                              currentPrice = 75 

                        elif(newRoomNums[7] <= 0):
                              print("No more Dexluxe King Rooms on floor 2")
                              noF2DeluxeKingRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Deluxe King Rooms available on floor 2")   
                  elif(floorAroom == "Floor 3 Deluxe King Room"):

                        if(newRoomNums[8] != 0):
                              newRoomNums[8] = newRoomNums[8] - 1  
                              roomIsReserved = True
                              print(floor2DKingRooms)
                              currentPrice = 75

                        elif (newRoomNums[8] <= 0):
                              print("No more Deluxe King Rooms on Floor 3")
                              noF3DeluxeKingRooms = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Deluxe King Rooms available on floor 3")   
                  #Corner King Room floor1CornerKingRooms
                  elif(floorAroom == "Floor 1 Corner King Room"):

                        if(newRoomNums[9] != 0):
                              newRoomNums[9] = newRoomNums[9] - 1
                              roomIsReserved = True
                              print(floor1CornerKingRooms)
                              currentPrice = 90  

                        elif(newRoomNums[9] <= 0):
                              print("No more Corner King Rooms on Floor 1")
                              noF1CornerKingRooms = True                                                                 
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner King Rooms available on floor 1")   

                  elif(floorAroom == "Floor 2 Corner King Room"):

                        if(newRoomNums[10] != 0):
                              newRoomNums[10] = newRoomNums[10] - 1
                              roomIsReserved = True
                              print(floor2CornerKingRooms)
                              currentPrice = 90

                        elif(newRoomNums[10] <= 0):
                              print("No more Corner King Rooms on Floor 2")   
                              noF2CornerKingRooms = True  
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner King Rooms available on floor 2")   

                  elif(floorAroom == "Floor 3 Corner King Room"):

                        if(newRoomNums[11] != 0):
                              newRoomNums[11] = newRoomNums[11] - 1
                              roomIsReserved = True
                              print(floor3CornerKingRooms)
                              currentPrice = 90

                        elif(newRoomNums[11] <= 0):
                              print("No more Corner King Rooms on Floor 3")   
                              noF3CornerKingRooms = True  
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner King Rooms available on floor 2")

                  #Corner Suite
                  elif(floorAroom == "Floor 1 Corner Suite"):

                        if(newRoomNums[12] != 0):
                              newRoomNums[12] = newRoomNums[12] - 1
                              roomIsReserved = True
                              print(floor1CornerSuites)
                              currentPrice = 110     

                        elif(newRoomNums[12] <= 0):
                              print("No more Corner Suites on Floor 1")
                              noF1CornerSuites = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner Suites available on floor 1")   

                  elif(floorAroom == "Floor 2 Corner Suite"):

                        if(newRoomNums[13] != 0):
                              newRoomNums[13] = newRoomNums[13] - 1
                              roomIsReserved = True
                              print(floor2CornerSuites)
                              currentPrice = 110

                        elif(newRoomNums[13] <= 0):
                              print("No more Corner Suites on Floor 2")
                              noF2CornerSuites = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner Suites available on floor 2")   
                              
                  elif(floorAroom == "Floor 3 Corner Suite"):

                        if(newRoomNums[14] != 0):
                              newRoomNums[14] = newRoomNums[14] - 1
                              roomIsReserved = True
                              print(floor3CornerSuites)
                              currentPrice = 110

                        elif(newRoomNums[14] <= 0):
                              print("No more Corner Suites on Floor 3")
                              noF3CornerSuites = True
                              messagebox.showinfo("Room Taken",
                              "There are no more Corner Suites available on floor 3")   
                              

                  #ask for receipt
                  if(roomIsReserved == True): #bool to check if a room was sucessfully reserved
                        receipt = messagebox.askquestion("receipt?",
                                                      "Do you want a receipt emailed to you?") #email to be implimented
                        

                        print(newRoomNums)

                        if (receipt == "yes"): #yes is given when the yes button is clicked
                              print("Receipt will be sent")
                              print(newRoomNums)

                              with open("File Handling/updatedRoomNums.txt", "w") as f: #write to file once values are updated
                                    for i in newRoomNums:
                                          f.write(str(i) + "\n") #write the new values as a string
                                    

                              with open("File Handling/totalPrice.txt", "r") as fp:
                                    totalPrice = fp.read()
                              fp.close()
                              totalPrice = int(totalPrice)
                              totalPrice = totalPrice + currentPrice

                              with open("File Handling/totalPrice.txt", "w") as fi:
                                    fi.write(str(totalPrice))

                              fi.close()

                              with open("File Handling/currentPrice.txt", "w") as fo:
                                    fo.write(str(currentPrice))

                              fo.close()



                              print("Number of King Rooms left on Floor 1: " + str(newRoomNums[0]))
                              print("Number of King Rooms left on Floor 2: " + str(newRoomNums[1]))
                              print("Number of King Rooms left on Floor 3: " + str(newRoomNums[2]))

                              print("Number of Twin Rooms left on Floor 1: " + str(newRoomNums[3]))
                              print("Number of Twim Rooms left on Floor 2: " + str(newRoomNums[4]))
                              print("Number of Twim Rooms left on Floor 3: " + str(newRoomNums[5]))

                              print("Number of Deluxe King Rooms left on Floor 1: " + str(newRoomNums[6]))
                              print("Number of Deluxe King Rooms left on Floor 2: " + str(newRoomNums[7]))
                              print("Number of Deluxe King Rooms left on Floor 3: " + str(newRoomNums[8]))

                              print("Number of Corner King Rooms left on Floor 1: " + str(newRoomNums[9]))
                              print("Number of Corner King Rooms left on Floor 2: " + str(newRoomNums[10]))
                              print("Number of Corner King Rooms left on Floor 3: " + str(newRoomNums[11]))

                              print("Number of Corner Suites left on Floor 1: " + str(newRoomNums[12]))
                              print("Number of Corner Suites left on Floor 2: " + str(newRoomNums[13]))
                              print("Number of Corner Suites left on Floor 3: " + str(newRoomNums[14])) 


                              

                              #destroy all widgets to exept the 
                              #cancel button in order to display the receipt
                              purchaseRoomButton.destroy()
                              floorOption_menu.destroy()
                              roomOption_menu.destroy()



                              #receipt text
                              thankYouLabel = Label(text="Thank You for Choosing to Stay with Rest-A-While Hotel",
                                                font=16,
                                          bg="#333130", fg="WHITE")
                              thankYouLabel.grid(row=2, column=2)

                              master.destroy()


                        else:
                              #no receipt
                              messagebox.showinfo("Receipt",
                                                "No receipt will be sent")

                              

                                          

#placeholder GUI until I pop off roomData once it is reserved 

                  #get the room that was already reserved

                  
      
        
        #Changes room image
        def changeImage(*args):
              room = roomOption_var.get()
              floor = floorOption_var.get()
              print(room)
              


      #Once a room is selected the user is show a preview of the room prior to them 
      #clicking the submit button
      #likely a better way to engineer this as it is repetative with all of 
      #the if statements

              if(room == "King Room"):
                    hotelLayoutLabel.destroy()

                    KingRLabel = Label(text="The cost of a King Room is $59.00 per night",
                                        bg="#333130", fg="WHITE")
                    KingRLabel.grid(row=2, column=2)


                    #Images
                    hotelPhoto = PhotoImage(file = "Images/bedroom.png")

                    KingRoomLabelI = Label(image = hotelPhoto)

                    KingRoomLabelI.image = hotelPhoto

                    KingRoomLabelI.grid(row=1, column=2)
          

              elif(room == "Twin Room"):
                    hotelLayoutLabel.destroy()

                    TwinRLabel = Label(text="The cost of a Twin Room is $69.00 per night",
                                        bg="#333130", fg="WHITE")
                    TwinRLabel.grid(row=2, column=2)

                    hotelPhoto = PhotoImage(file = "Images/bedroom1.png")

                    TwinRoomLabelI = Label(image = hotelPhoto)

                    TwinRoomLabelI.image = hotelPhoto

                    TwinRoomLabelI.grid(row=1, column=2)

              elif(room == "Deluxe King Room"):
                    hotelLayoutLabel.destroy()

                    DeluxeKingRLabel = Label(text="The cost of a Dexluxe King Room is $75 per night",
                                              bg="#333130", fg="WHITE")
                    DeluxeKingRLabel.grid(row=2, column=2)

                    hotelPhoto = PhotoImage(file = "Images/bedroom2.png")

                    DeluxeKingRoomLabelI = Label(image = hotelPhoto)

                    DeluxeKingRoomLabelI.image = hotelPhoto

                    DeluxeKingRoomLabelI.grid(row=1, column=2)

              elif(room == "Corner Room"):
                    hotelLayoutLabel.destroy()

                    CornerRLabel = Label(text="The cost of a Corner Room is $75 per night",
                                              bg="#333130", fg="WHITE")
                    
                    CornerRLabel.grid(row=2, column=2)

                    hotelPhoto = PhotoImage(file = "Images/bedroom3.png")

                    CornerRoomLabelI = Label(image = hotelPhoto)

                    CornerRoomLabelI.image = hotelPhoto

                    CornerRoomLabelI.grid(row=1, column=2)

              elif(room == "Corner King Room"):
                    hotelLayoutLabel.destroy()

                    CornerKingRLabel = Label(text="The cost of a Corner King Room is $90 per night",
                                          bg="#333130", fg="WHITE")

                    CornerKingRLabel.grid(row=2, column=2)
                  

                    hotelPhoto = PhotoImage(file = "Images/bedroom4.png")

                    CornerKingRoomLabelI = Label(image = hotelPhoto)

                    CornerKingRoomLabelI.image = hotelPhoto

                    CornerKingRoomLabelI.grid(row=1, column=2)

              elif(room == "Corner Suite"):
                    hotelLayoutLabel.destroy()

                    CornerSuiteLabel = Label(text="The cost of a Corner Suite is $110 per night",
                                                bg="#333130", fg="WHITE")
                    CornerSuiteLabel.grid(row=2, column=2)

                    hotelPhoto = PhotoImage(file = "Images/bedroom5.png")

                    CornerKingRoomLabelI = Label(image = hotelPhoto)

                    CornerKingRoomLabelI.image = hotelPhoto

                    CornerKingRoomLabelI.grid(row=1, column=2)
              


        #Creating Labels 

        headerLabel = Label(master, text="Rest-A-While", fg="WHITE",
                            bg="#333130", font=("Courier", 20))
        headerLabel.grid(row=1,column=1)


        #creating buttons

        purchaseRoomButton = Button(text="Purchase", bg="BLACK", fg="WHITE",
                                    height=3, width=15,
                                    activebackground="#4d231f",
                                     command=purchaseRoomSelection,
                                     state=DISABLED)
        purchaseRoomButton.grid(row=7, column=1)


        #Creating Drop Down Menus


      #floorOptionList

        def normalRoomOptionMenu(*args): #pass in if a room is already reserved
    
            floorO = floorOption_var.get()

            if (floorO == "Floor 1"\
                  or floorO == "Floor 2"\
                  or floorO == "Floor 3"):

                  roomOption_menu.configure(state=NORMAL)

        def normalSectionOptionMenu(*args):

              roomO = roomOption_var.get()

              if (roomO == "King Room"\
                    or roomO == "Twin Room"\
                    or roomO == "Deluxe King Room"\
                    or roomO == "Corner King Room"\
                    or roomO == "Corner Suite"):

                    purchaseRoomButton.configure(state=NORMAL)

        floorOptionList = ("Floor 1", "Floor 2", "Floor 3")

        floorOption_var = StringVar()

        floorOption_var.set("Floor Selection") #set to the fisrt value in the drop down menu
        
        floorOption_menu = OptionMenu(master, floorOption_var, *floorOptionList, command=normalRoomOptionMenu)
        floorOption_menu.grid(row = 3, column = 2, sticky="W")
        floorOption_menu.configure(bg="BLACK", fg="WHITE",
                              width = 15, height = 2,
                              bd=3, #items within the menu's width
                              activebackground="#4d231f")



        #Room option list

        roomOptionList = ("King Room", "Twin Room", "Deluxe King Room",
                        "Corner Room", "Corner King Room", "Corner Suite")

        roomOption_var = StringVar()
        roomOption_var.set("Room Selection") #set to the fisrt value in the drop down menu
        roomOption_var.trace("w", changeImage)
        
        roomOption_menu = OptionMenu(master, roomOption_var, *roomOptionList, command=normalSectionOptionMenu)
        roomOption_menu.grid(row = 3, column = 2, sticky = "E") 
        roomOption_menu.configure(bg="BLACK", fg="WHITE",
                        width = 15, height = 2,
                        activebackground="#4d231f",
                        bd=3,
                        state=DISABLED)
