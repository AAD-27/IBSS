import tkinter as tk
from tkinter import ttk
import tkinter as tk        
from PIL import Image, ImageTk
  
# Creating tkinter window
root = tk.Tk ()  
root.title('Inverter Battery Selection Software')
root.geometry('1500x850')
root.config(bg = "khaki1")
 
#Creating variables for gui
ame = tk.StringVar()
cfl  = tk.IntVar()
tube = tk.IntVar()
fan  = tk.IntVar()
dish = tk.IntVar()
lcd = tk.IntVar()
computer = tk.IntVar()

#Baground
image1 = Image.open("AC.PNG")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test


label1.place(x=1, y=15)                                 # Position image

#Main title
ttk.Label(root, text = "Inverter Battery Selection Software",background = "khaki1",font = ("Times New Roman", 22)).grid(column = 2,row = 0, padx = 10, pady = 25)
ttk.Label(root, text = "Customer Name  ",background = "khaki1",font = ("Times New Roman", 15)).grid(column = 0,row = 1, padx = 10, pady = 25)
ent = ttk.Entry(root,width = 40,  textvariable = ame)
ent.grid(column = 1,row = 1, padx = 10, pady = 25)

#Labels for titles
ttk.Label(root, text = "Appliances", borderwidth = 3, background = "khaki1",font = ("Times New Roman", 14)).grid(column = 0,row = 2, padx = 10, pady = 25)
ttk.Label(root, text = "Quantity",background = "khaki1",font = ("Times New Roman", 14)).grid(column = 1,row = 2, padx = 10, pady = 25)                     #Combobox creation
ttk.Label(root, text = "Approximate Wattage",background = "khaki1",font = ("Times New Roman", 14)).grid(column = 2,row = 2, padx = 10, pady = 1)  

#=============================================================================

#Landing Battery Image
image1 = Image.open("AD.PNG")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

label1.place(x=923, y=300)

#------------------------------------------------------------------------------

#1st Appliance
lbl_cfl = ttk.Label(root, text = "CFL - Large" ,background = "khaki1", anchor="w",borderwidth = 2, justify = "left", border=10 , font = ("Times New Roman", 11)).grid(column = 0,row = 3, padx = 10, pady = 25)
  
combo_cfl = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = cfl)                    #Combobox creation
  
# Adding combobox drop down list
combo_cfl['values'] = (0,1,2,3,4,5,6,7,8,9,10)  
combo_cfl.grid(column = 1, row = 3)
lbl1 = ttk.Label(root, text = 30 ,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 3, padx = 10, pady = 25) 
combo_cfl.current()

#------------------------------------------------------------------------------

#2nd Appliance
lbl_tube = ttk.Label(root, text = "Tube Light ",justify = "left",anchor="w",background = "khaki1",font = ("Times New Roman", 11)).grid(column = 0,row = 4, padx = 10, pady = 25)
  
combo_tube = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = tube)                    #Combobox creation
lbl3 = ttk.Label(root, text = 60,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 4, padx = 10, pady = 25)  

 
# Adding combobox drop down list
combo_tube['values'] = (0,1,2,3,4,5,6,7,8,9,10)
  
combo_tube.grid(column = 1, row = 4)
combo_tube.current()

#------------------------------------------------------------------------------

#3rd Appliance
 
lbl_fan = ttk.Label(root, text = "Fan ",background = "khaki1",justify = "left",font = ("Times New Roman", 11)).grid(column = 0,row = 5, padx = 10, pady = 25)
  
combo_fan = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = fan)                    #Combobox creation
combo_fan.grid(column = 1, row = 5)
lbl3 = ttk.Label(root, text = 100,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 5, padx = 10, pady = 25)  

 
# Adding combobox drop down list
combo_fan['values'] = (0,1,2,3,4,5,6,7,8,9,10)
 
combo_fan.current()

#------------------------------------------------------------------------------

#4th Appliance
lbl_dish = ttk.Label(root, text = "Satellite / Dish TV Connection ",anchor="w",justify = "left",background = "khaki1",font = ("Times New Roman", 11)).grid(column = 0,row =6, padx = 10, pady = 25)
  
combo_dish = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = dish)                    #Combobox creation
combo_dish.grid(column = 1, row = 6)
lbl3 = ttk.Label(root, text = 100,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 6, padx = 10, pady = 25)  
 
# Adding combobox drop down list
combo_dish['values'] = (0,1,2,3,4,5,6,7,8,9,10)
 
combo_dish.current()

#------------------------------------------------------------------------------

#5th Appliance
lbl_lcd = ttk.Label(root, text = "LCD TV up to 32 inch ",justify = "left",background = "khaki1",font = ("Times New Roman", 11)).grid(column = 0,row = 7, padx = 10, pady = 25)
batteryBox = ttk.Label(root, text = "--Recommended Battery (60 mins back-up)--",justify = "left",background = "khaki1",font = ("Times New Roman", 15)).grid(column = 4,row = 8, padx = 10, pady = 25)  
combo_lcd = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = lcd)                    #Combobox creation
combo_lcd.grid(column = 1, row = 7)
lbl3 = ttk.Label(root, text = 150,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 7, padx = 10, pady = 25)  

 
# Adding combobox drop down list
combo_lcd['values'] = (0,1,2,3,4,5,6,7,8,9,10)
 
combo_lcd.current()

#------------------------------------------------------------------------------

#6th Appliance
lbl_computer = ttk.Label(root, text = "Computer with monitor - max 20 in",justify = "left",background = "khaki1",font = ("Times New Roman", 11)).grid(column = 0,row = 8, padx = 10, pady = 25)
  
lbl_computer = ttk.Combobox(root,background = "khaki1", width = 27, textvariable = computer)                    #Combobox creation
lbl_computer.grid(column = 1, row =8)
lbl3 = ttk.Label(root, text = 450,background = "khaki1",font = ("Times New Roman", 12)).grid(column = 2,row = 8, padx = 10, pady = 25)  

 
# Adding combobox drop down list
lbl_computer['values'] = (0,1,2,3,4,5,6,7,8,9,10)
 
lbl_computer.current()
 
#---------------------------------------------------------------------------------

#Calculations 
def but( ): 

    a1 = cfl.get()
    a1 = a1 * 30
    a2 = tube.get()
    a2 = a2 * 60
    a3 = fan.get()
    a3 = a3 * 100
    a4 = dish.get()
    a4 = a4 * 100
    a5 = lcd.get()
    a5 = a5 * 150
    a6 = computer.get()
    a6 = a6 * 300    

    total = a1+a2+a3+a4+a5+a6
    print("\nTotal load in Watts is     ",total,"W")   
    
#creating gui for image 
    if total > 1000:
        # Create a photoimage object of the image in the path
        image1 = Image.open("3.PNG")
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=923, y=300)
    
    elif total > 600:
        # Create a photoimage object of the image in the path
        image1 = Image.open("2.PNG")
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=923, y=300)


    else:
        # Create a photoimage object of the image in the path
        image1 = Image.open("1.PNG")
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=923, y=300)
    root.mainloop()

#=========================================================
#Database
def base():
    import sqlite3                                           # Connect to sqlite database
    conn = sqlite3.connect('students.db')       
    print("\n\nDatabase Created")

    cursor = conn.cursor()                                   #used cursor to point to the database connection
    

    def data():
        a1 = cfl.get()
        a1 = a1 * 30
        a2 = tube.get()
        a2 = a2 * 60
        a3 = fan.get()
        a3 = a3 * 100
        a4 = dish.get()
        a4 = a4 * 100
        a5 = lcd.get()
        a5 = a5 * 150
        a6 = computer.get()
        a6 = a6 * 450    
         
        name = ame.get()
 
        cursor.execute('CREATE TABLE IF NOT EXISTS final ( Name TEXT, A1 REAL , A2 REAL , A3 REAL ,A4 REAL , A5 REAL, A6 REAL)')
        
        print("\nTable created successfully ")

        
        cursor.execute("INSERT INTO final (Name,A1,A2,A3,A4,A5,A6) VALUES(?, ?,?,?,?,?,?)", (name,a1,a2,a3,a4,a5,a6))


        conn.commit()

    print("\nRecords inserted........")
    
    data()
    print("\nReading Records.......")
    print("Name,CFL,Tube,Fan,LCD,Dish,Computer\n\n")
    cursor = conn.execute("SELECT * from final")
    result = cursor.fetchall()
    print(result, end = "\n")
    print("----------------------------------------------------------------------")

#Buttons     
b1 = ttk.Button(root,text = "\n         Submit       \n", command = but )    #command calls the function
b1.grid(column = 1,row = 13)                                                 #packing button

b2 = ttk.Button(root,text = "Click here to update database", command = base)
b2.grid(column = 0, row = 14)

#Exit Code
def iExit():

    root.destroy()
    return

b3 = ttk.Button(root,text = "\n          Exit         \n", command =iExit)
b3.grid(column = 2,row = 13)    

def clearForm():
    cfl.set(0)   
    tube.set(0)    
    fan.set(0)
    dish.set(0)
    lcd.set(0)
    computer.set(0)
    image1 = Image.open("AD.PNG")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test

 
    label1.place(x=923, y=300)

b4 = ttk.Button(root,text = "Clear form", command=  clearForm)
b4.grid(column = 0,row = 13)    

root.mainloop()
 
 