# Imports
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import numpy as np
import pandas as pd

# Import CSV file
GuessWho_DB = pd.read_csv("GuessWhoCSV.csv")
Positions_DB = pd.read_csv("CharacterPositions.csv")

# Create the game window
window = Tk()
window.title("Guess Who?")
window.state("zoomed")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# Characters directories
Alex_Image = Image.open(r'D:\Guess Who\Character Images\Alex.png')
Alex_Image = Alex_Image.resize((135, 320))
Alex_Image = ImageTk.PhotoImage(Alex_Image)
Alfred_Image = Image.open(r'D:\Guess Who\Character Images\Alfred.png')
Alfred_Image = Alfred_Image.resize((135, 320))
Alfred_Image = ImageTk.PhotoImage(Alfred_Image)
Anita_Image = Image.open(r'D:\Guess Who\Character Images\Anita.png')
Anita_Image = Anita_Image.resize((135, 320))
Anita_Image = ImageTk.PhotoImage(Anita_Image)
Anne_Image = Image.open(r'D:\Guess Who\Character Images\Anne.png')
Anne_Image = Anne_Image.resize((135, 320))
Anne_Image = ImageTk.PhotoImage(Anne_Image)
Bernard_Image = Image.open(r'D:\Guess Who\Character Images\Bernard.png')
Bernard_Image = Bernard_Image.resize((135, 320))
Bernard_Image = ImageTk.PhotoImage(Bernard_Image)
Bill_Image = Image.open(r'D:\Guess Who\Character Images\Bill.png')
Bill_Image = Bill_Image.resize((135, 320))
Bill_Image = ImageTk.PhotoImage(Bill_Image)
Charles_Image = Image.open(r'D:\Guess Who\Character Images\Charles.png')
Charles_Image = Charles_Image.resize((135, 320))
Charles_Image = ImageTk.PhotoImage(Charles_Image)
Claire_Image = Image.open(r'D:\Guess Who\Character Images\Claire.png')
Claire_Image = Claire_Image.resize((135, 320))
Claire_Image = ImageTk.PhotoImage(Claire_Image)
David_Image = Image.open(r'D:\Guess Who\Character Images\David.png')
David_Image = David_Image.resize((135, 320))
David_Image = ImageTk.PhotoImage(David_Image)
Eric_Image = Image.open(r'D:\Guess Who\Character Images\Eric.png')
Eric_Image = Eric_Image.resize((135, 320))
Eric_Image = ImageTk.PhotoImage(Eric_Image)
Frans_Image = Image.open(r'D:\Guess Who\Character Images\Frans.png')
Frans_Image = Frans_Image.resize((135, 320))
Frans_Image = ImageTk.PhotoImage(Frans_Image)
George_Image = Image.open(r'D:\Guess Who\Character Images\George.png')
George_Image = George_Image.resize((135, 320))
George_Image = ImageTk.PhotoImage(George_Image)
Herman_Image = Image.open(r'D:\Guess Who\Character Images\Herman.png')
Herman_Image = Herman_Image.resize((135, 320))
Herman_Image = ImageTk.PhotoImage(Herman_Image)
Joe_Image = Image.open(r'D:\Guess Who\Character Images\Joe.png')
Joe_Image = Joe_Image.resize((135, 320))
Joe_Image = ImageTk.PhotoImage(Joe_Image)
Maria_Image = Image.open(r'D:\Guess Who\Character Images\Maria.png')
Maria_Image = Maria_Image.resize((135, 320))
Maria_Image = ImageTk.PhotoImage(Maria_Image)
Max_Image = Image.open(r'D:\Guess Who\Character Images\Max.png')
Max_Image = Max_Image.resize((135, 320))
Max_Image = ImageTk.PhotoImage(Max_Image)
Paul_Image = Image.open(r'D:\Guess Who\Character Images\Paul.png')
Paul_Image = Paul_Image.resize((135, 320))
Paul_Image = ImageTk.PhotoImage(Paul_Image)
Peter_Image = Image.open(r'D:\Guess Who\Character Images\Peter.png')
Peter_Image = Peter_Image.resize((135, 320))
Peter_Image = ImageTk.PhotoImage(Peter_Image)
Phillip_Image = Image.open(r'D:\Guess Who\Character Images\Phillip.png')
Phillip_Image = Phillip_Image.resize((135, 320))
Phillip_Image = ImageTk.PhotoImage(Phillip_Image)
Richard_Image = Image.open(r'D:\Guess Who\Character Images\Richard.png')
Richard_Image = Richard_Image.resize((135, 320))
Richard_Image = ImageTk.PhotoImage(Richard_Image)
Robert_Image = Image.open(r'D:\Guess Who\Character Images\Robert.png')
Robert_Image = Robert_Image.resize((135, 320))
Robert_Image = ImageTk.PhotoImage(Robert_Image)
Sam_Image = Image.open(r'D:\Guess Who\Character Images\Sam.png')
Sam_Image = Sam_Image.resize((135, 320))
Sam_Image = ImageTk.PhotoImage(Sam_Image)
Susan_Image = Image.open(r'D:\Guess Who\Character Images\Susan.png')
Susan_Image = Susan_Image.resize((135, 320))
Susan_Image = ImageTk.PhotoImage(Susan_Image)
Tom_Image = Image.open(r'D:\Guess Who\Character Images\Tom.png')
Tom_Image = Tom_Image.resize((135, 320))
Tom_Image = ImageTk.PhotoImage(Tom_Image)
X_Image = Image.open(r'D:\Guess Who\Character Images\X.png')
X_Image = X_Image.resize((135, 320))
X_Image = ImageTk.PhotoImage(X_Image)
# Establish Fonts
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 12))
helv60 = font.Font(family='Helvetica', size=60, weight='bold')
Board_Text_Font = font.Font(family='Helvetica', size=30)
helv20 = font.Font(family='Helvetica', size=20)
helv12 = font.Font(family='Helvetica', size=12)
# Possible Characters - Might switch for a pandas column selector for easier access
Character_List = [ "Alex", "Alfred", "Anita", "Anne", "Bernard", "Bill", "Charles", "Claire", "David", "Eric", "Frans", "George", "Herman", "Joe", "Maria", "Max", "Paul", "Peter", "Phillip", "Richard", "Robert", "Sam", "Susan", "Tom"]
Possible_Characters = ["Alex", "Alfred", "Anita", "Anne", "Bernard", "Bill", "Charles", "Claire", "David", "Eric", "Frans", "George", "Herman", "Joe", "Maria", "Max", "Paul", "Peter", "Phillip", "Richard", "Robert", "Sam", "Susan", "Tom"]
Computer_Difficulties = ["Easy(10 Guesses)", "Medium(8 Guesses)", "Hard(5 Guesses)"] 
Player_Wincount = 0
Computer_Wincount = 0

def Generate_Random_Characters():
    global Human_Mystery_Character
    global Computer_Mystery_Character
    Human_Mystery_Character = random.choice(Character_List)
    Computer_Mystery_Character = random.choice(Character_List)

# Function for creating a blank new screen
def New_Screen():
    global mainframe
    mainframe.destroy()
    mainframe = ttk.Frame(window)
    mainframe.pack(fill="both", expand=True)

# Main screen with play button
def Start_Screen():
    global Start_Text
    global mainframe
    global Computer_Difficulty
    Start_Screen_Displayed = True
    mainframe = ttk.Frame(window, width=60, height=40) 
    mainframe.grid(column=0, row=0, padx=20, pady=20)
    Start_Text = ttk.Label(mainframe, text="Guess Who?", font=helv60).grid(column=0, row=0)
    SS_Label = ttk.Label(mainframe, text="Computer Difficulty:", font=helv20).grid(column=0,row=1)
    Computer_Difficulty = tk.StringVar(mainframe)
    Computer_Difficulty_OptionMenu = tk.OptionMenu(mainframe, Computer_Difficulty, *Computer_Difficulties)
    Computer_Difficulty_OptionMenu.grid(column=0,row=2)
    Computer_Difficulty.set("Select Difficulty")
    Computer_Difficulty_OptionMenu.config(font=helv12)
    Play_Button = ttk.Button(mainframe, text="Play!", command=Board_Screen).grid(column=0,row=3)
# System for when user makes a guess
def guess_callback():
    global Turn_Count
    global Computer_Mystery_Character
    Turn_Count+=1
    selection = Guess_Option.get()
    False_Characters_List = []
    True_Characters_List = []
    True_Characters = GuessWho_DB[GuessWho_DB[selection] == True]
    for i in True_Characters.index:
        True_Characters_List.append(i)
    False_Characters = GuessWho_DB[GuessWho_DB[selection] == False]
    for i in False_Characters.index:
        False_Characters_List.append(i)
    if Computer_Mystery_Character in False_Characters_List:
        for i in True_Characters_List:
            X_Label = ttk.Label(mainframe, image=X_Image)
            X_Pos = Positions_DB.loc[i, "x"]
            Y_Pos = Positions_DB.loc[i, "y"]
            if Y_Pos == 7:
                X_Label.grid(column=Y_Pos, row=X_Pos, padx=(0,140))
            else:
                X_Label.grid(column=Y_Pos, row=X_Pos)
    else:
        for i in False_Characters_List:
            X_Label = ttk.Label(mainframe, image=X_Image)
            X_Pos = Positions_DB.loc[i, "x"]
            Y_Pos = Positions_DB.loc[i, "y"]          
            if Y_Pos == 7:
                X_Label.grid(column=Y_Pos, row=X_Pos, padx=(0,140))
            else:
                X_Label.grid(column=Y_Pos, row=X_Pos)
    Turn_Display_Label = ttk.Label(Turns_Frame, text="Computer Will Guess your Mystery Character In: " + str(Allowed_Turns - Turn_Count) + " Turns", font=helv12).grid(column=0,row=0)           
def final_guess_callback():
    global Player_Wincount
    global Computer_Wincount
    global Computer_Mystery_Character
    final_selection = Final_Guess_Option.get()
    if Player_Wincount or Computer_Wincount >= 1:
        global Championship_Continue_Screen
        global Championship_Prompt_Screen
        if Player_Wincount or Computer_Wincount == 5:
            Determine_Winner()
        elif final_selection == Computer_Mystery_Character:
            Player_Wincount+=1
            Championship_Continue_Screen()
        else:
            Computer_Wincount+=1
            Championship_Continue_Screen()
    else:
        if final_selection == Computer_Mystery_Character:
            Player_Wincount+=1
            Championship_Prompt_Screen()
        else:
            Computer_Wincount+=1
            Championship_Prompt_Screen()

def Determine_Winner():
    global Computer_Wincount
    global Player_Wincount
    if Player_Wincount == 5:
        Player_Win_Screen()
    else:
        Computer_Win_Screen()

def Player_Win_Screen():
    global mainframe
    for widget in mainframe.winfo_children():
        widget.destroy()
    mainframe.destroy()
    mainframe = ttk.Frame(window, width=60, height=40) 
    mainframe.grid(column=0, row=0, padx=20, pady=20)
    PWS_Label_One = ttk.Label(mainframe, text="Congratulations you have beat the computer on " + Dif_Var + " mode!", font=helv20).grid(column=0,row=0)
    PWS_Button = ttk.Button(mainframe, text="Exit Game",style='my.TButton', command= window.destroy).grid(column=0,row=1)

def Computer_Win_Screen():
    global mainframe
    for widget in mainframe.winfo_children():
        widget.destroy()
    mainframe.destroy()
    mainframe = ttk.Frame(window, width=60, height=40) 
    mainframe.grid(column=0, row=0, padx=20, pady=20)
    CWS_Label_One = ttk.Label(mainframe, text="The computer beat you on " + Dif_Var + " mode! Better luck next time", font=helv20).grid(column=0,row=0)
    CWS_Button = ttk.Button(mainframe, text="Exit Game",style='my.TButton', command= window.destroy).grid(column=0,row=1)

def Championship_Prompt_Screen():
    global mainframe
    for widget in mainframe.winfo_children():
        widget.destroy()
    mainframe.destroy()
    mainframe = ttk.Frame(window, width=60, height=40) 
    mainframe.grid(column=0, row=0, padx=20, pady=20)
    CPS_Label_One = ttk.Label(mainframe, text="Computer has won " + str(Computer_Wincount)+ " games.", font=helv20).grid(column=0,row=0)
    CPS_Label_Two = ttk.Label(mainframe, text="Player has won " + str(Player_Wincount) + " games.", font=helv20).grid(column=0,row=1)
    CPS_Button = ttk.Button(mainframe, text="Play a first to 5 Championship Series?",style='my.TButton', command= Board_Screen).grid(column=0,row=2)

def Championship_Continue_Screen():
    global mainframe
    for widget in mainframe.winfo_children():
        widget.destroy()
    mainframe.destroy()
    mainframe = ttk.Frame(window, width=60, height=40) 
    mainframe.grid(column=0, row=0, padx=20, pady=20)
    CCS_Label_One = ttk.Label(mainframe, text="Computer has won " + str(Computer_Wincount) + " games.", font=helv20).grid(column=0,row=0)
    CCS_Label_Two = ttk.Label(mainframe, text="Player has won " + str(Player_Wincount) + " games.", font=helv20).grid(column=0,row=1)
    CCS_Button = ttk.Button(mainframe, text="Next Game",style='my.TButton', command= Board_Screen).grid(column=0,row=2)

Alex_X = 0
Alfred_X = 0
Anita_X = 0
Anne_X = 0
Bernard_X = 0
Bill_X = 0
Charles_X = 0
Claire_X = 0
David_X = 1
Eric_X = 1
Frans_X = 1
George_X = 1
Herman_X = 1
Joe_X = 1
Maria_X = 1
Max_X = 1
Paul_X = 2
Peter_X = 2
Phillip_X = 2
Richard_X = 2
Robert_X = 2
Sam_X = 2
Susan_X = 2
Tom_X = 2
Alex_Y = 0
Alfred_Y = 1
Anita_Y = 2
Anne_Y = 3
Bernard_Y = 4
Bill_Y = 5
Charles_Y = 6
Claire_Y = 7
David_Y = 0
Eric_Y = 1
Frans_Y = 2
George_Y = 3
Herman_Y = 4
Joe_Y = 5
Maria_Y = 6
Max_Y = 7
Paul_Y = 0
Peter_Y = 1
Phillip_Y = 2
Richard_Y = 3
Robert_Y = 4
Sam_Y = 5
Susan_Y = 6
Tom_Y = 7

def Difficulty():
    global Dif_Var
    global Allowed_Turns
    Difficulty_Selection = Computer_Difficulty.get()
    if Difficulty_Selection == "Hard(5 Guesses)":
        Allowed_Turns = 5
        Dif_Var = "Hard"
    elif Difficulty_Selection == "Medium(8 Guesses)":
        Allowed_Turns = 8
        Dif_Var = "Medium"
    else:
        Allowed_Turns = 10
        Dif_Var = "Easy"

# Creates the main board with the character images
def Board_Screen():
    global Turns_Frame
    global Turn_Count
    global Guess_Option
    global Final_Guess_Option
    Turn_Count = 0
    Difficulty()
    Generate_Random_Characters()
    New_Screen()
    s = ttk.Style()
    s.configure('TFrame', background='#f0f0f0')
    Alex_Label = ttk.Label(mainframe, image=Alex_Image).grid(column=Alex_Y, row=Alex_X)
    Alfred_Label = ttk.Label(mainframe, image=Alfred_Image).grid(column=Alfred_Y, row=Alfred_X)
    Anita_Label = ttk.Label(mainframe, image=Anita_Image).grid(column=Anita_Y, row=Anita_X)
    Anne_Label = ttk.Label(mainframe, image=Anne_Image).grid(column=Anne_Y, row=Anne_X)
    Bernard_Label = ttk.Label(mainframe, image=Bernard_Image).grid(column=Bernard_Y, row=Bernard_X)
    Bill_Label = ttk.Label(mainframe, image=Bill_Image).grid(column=Bill_Y, row=Bill_X)
    Charles_Label = ttk.Label(mainframe, image=Charles_Image).grid(column=Charles_Y, row=Charles_X)
    Claire_Label = ttk.Label(mainframe, image=Claire_Image).grid(column=Claire_Y, row=Claire_X, padx=(0,140))
    David_Label = ttk.Label(mainframe, image=David_Image).grid(column=David_Y, row=David_X)
    Eric_Label = ttk.Label(mainframe, image=Eric_Image).grid(column=Eric_Y, row=Eric_X)
    Frans_Label = ttk.Label(mainframe, image=Frans_Image).grid(column=Frans_Y, row=Frans_X)
    George_Label = ttk.Label(mainframe, image=George_Image).grid(column=George_Y, row=George_X)
    Herman_Label = ttk.Label(mainframe, image=Herman_Image).grid(column=Herman_Y, row=Herman_X)
    Joe_Label = ttk.Label(mainframe, image=Joe_Image).grid(column=Joe_Y, row=Joe_X)
    Maria_Label = ttk.Label(mainframe, image=Maria_Image).grid(column=Maria_Y, row=Maria_X)
    Max_Label = ttk.Label(mainframe, image=Max_Image).grid(column=Max_Y, row=Max_X, padx=(0,140))
    Paul_Label = ttk.Label(mainframe, image=Paul_Image).grid(column=Paul_Y, row=Paul_X)
    Peter_Label = ttk.Label(mainframe, image=Peter_Image).grid(column=Peter_Y, row=Peter_X)
    Phillip_Label = ttk.Label(mainframe, image=Phillip_Image).grid(column=Phillip_Y, row=Phillip_X)
    Richard_Label = ttk.Label(mainframe, image=Richard_Image).grid(column=Richard_Y, row=Richard_X)
    Robert_Label = ttk.Label(mainframe, image=Robert_Image).grid(column=Robert_Y, row=Robert_X)
    Sam_Label = ttk.Label(mainframe, image=Sam_Image).grid(column=Sam_Y, row=Sam_X)
    Susan_Label = ttk.Label(mainframe, image=Susan_Image).grid(column=Susan_Y, row=Susan_X)
    Tom_Label = ttk.Label(mainframe, image=Tom_Image).grid(column=Tom_Y, row=Tom_X, padx=(0,140))
    # Seperating characters from buttons
    Board_Seperator = ttk.Separator(mainframe, orient=VERTICAL)
    Board_Seperator.place(relx=0.59, rely=0, relwidth=0.5, relheight=1)
    # Label and OptionMenu To allow user to guess
    Access_Frame = ttk.Frame(mainframe)
    Access_Frame.grid(column=8,row=0, sticky=NW)
    Guess_Frame = ttk.Frame(Access_Frame, borderwidth=10, relief="ridge")
    Guess_Frame.grid(column=0,row=1, sticky=NW, pady=(30,30))
    FGuess_Frame = ttk.Frame(Access_Frame, borderwidth=10, relief="ridge")
    FGuess_Frame.grid(column=0,row=2, sticky=NW, pady=(30,30))
    Turns_Frame = ttk.Frame(Access_Frame, borderwidth=10, relief="ridge")
    Turns_Frame.grid(column=0,row=3, sticky=NW, pady=(30,30))

    Guess_Label_One = ttk.Label(Guess_Frame, text="Does your character have", font=helv20).grid(column=0,row=0, sticky=W)
    Access_Frame.columnconfigure(0, minsize=120)
    Guess_Option = tk.StringVar(Guess_Frame)
    Guess_Optionmenu = tk.OptionMenu(Guess_Frame, Guess_Option, *GuessWho_DB.columns)
    Guess_Optionmenu.grid(column=1,row=0, sticky=W)
    Guess_Option.set("Select Guess")
    Guess_Optionmenu.config(font=helv20)
    Guess_Label_Two = ttk.Label(Guess_Frame, text="?", font=helv20).grid(column=2,row=0, sticky=W)
    # Button to sumbit guess
    Submit_Guess = ttk.Button(Guess_Frame, text="Submit Guess", command=guess_callback)
    Submit_Guess.grid(column=3, row=0, sticky=W)
    # Label and OptionMenu to allow user to make their final guess
    Final_Guess_Label_One = ttk.Label(FGuess_Frame, text="Is your character", font=helv20).grid(column=0,row=1, sticky=W)
    Final_Guess_Option = tk.StringVar(FGuess_Frame)
    Final_Guess_OptionMenu = tk.OptionMenu(FGuess_Frame, Final_Guess_Option, *Possible_Characters)
    Final_Guess_OptionMenu.grid(column=1,row=1, sticky=W)
    Final_Guess_Option.set("Select Guess")
    Final_Guess_OptionMenu.config(font=helv20)
    Final_Guess_Label_Two = ttk.Label(FGuess_Frame,text="?", font=helv20).grid(column=2,row=1, sticky=W)
    # Button to submit final guess
    Submit_Final_Guess= ttk.Button(FGuess_Frame, text="Make Your Final Guess", command=final_guess_callback)
    Submit_Final_Guess.grid(column=3, row=1, sticky=W)
    Turn_Display_Label = ttk.Label(Turns_Frame, text="Computer Will Guess your Mystery Character In: " + str(Allowed_Turns) + " Turns", font=helv12).grid(column=0,row=0, sticky=W)
    
Positions_DB.set_index("Name", inplace = True)
GuessWho_DB.set_index("Name", inplace = True)

# Start Screen 
Start_Screen()

# Run program
window.mainloop()
