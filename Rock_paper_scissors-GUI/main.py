##Author:- Rohit Kavitake.

##importing modules..
import random
from tkinter import *
import tkinter
#from tkinter.ttk import *


Message = ""
win = "Congo You WIN :*"
lose = " Better Luck Next Time :)"
tie = "Its a tie :0 "

root = Tk()
root.geometry("350x300")
rock = PhotoImage(file="stone.gif")
paper = PhotoImage(file="paper.gif")
scissors = PhotoImage(file="scissors.gif")


elements = [rock , paper, scissors]




def Rock():
    CPUChoice = random.choice(elements)
    playerChoice = '1'
    lbl = Label(root,text="CPU Choice ::")
    lbl.place(x=0,y=150)
    cpc = Label(root,image=CPUChoice)
    cpc.place(x=150,y=150)
    if playerChoice == '1' and CPUChoice == rock:
        result = tie
        resultText.set('You and the CPU both picked rock. ' + result)
        
    if playerChoice == '1' and CPUChoice == paper:
        result = lose
        resultText.set('Paper beats rock. ' + result)
        
    if playerChoice == '1' and CPUChoice == scissors:
        result = win
        resultText.set('Rock smashes scissors. ' + result)
    

def Paper():
    CPUChoice =random.choice(elements)
    playerChoice = '2'
    lbl = Label(root,text="CPU Choice ::")
    lbl.place(x=0,y=150)
    cpc = Label(root,image=CPUChoice)
    cpc.place(x=150,y=150)
    if playerChoice == '2' and CPUChoice == rock:
        result = win
        resultText.set('Paper beats rock. ' + result)
        
    if playerChoice == '2' and CPUChoice == paper:
        result = tie
        resultText.set('You and the CPU both picked paper ' + result)
        
    if playerChoice == '2' and CPUChoice == scissors:
        result = lose
        resultText.set('Scissors cuts up paper. ' + result)

def Scissors():
    CPUChoice = random.choice(elements)
    playerChoice = '3'
    lbl = Label(root,text="CPU Choice ::")
    lbl.place(x=0,y=150)
    cpc = Label(root,image=CPUChoice)
    cpc.place(x=150,y=150)
    if playerChoice == '3' and CPUChoice == rock:
        result = lose
        resultText.set('Rock smashes scissors. ' + result)
        
    if playerChoice == '3' and CPUChoice == paper:
        result = win
        resultText.set('Scissors cuts up paper. ' + result)
        
    if playerChoice == '3' and CPUChoice == scissors:
        result = tie
        resultText.set('You and the CPU both picked scissors. ' + result)
    lbl.destroy



widgetRock = Button(root, command=Rock, width=40, height=35, image=rock)
widgetRock.place(x=35,y=10)

widgetPaper = Button(root, command=Paper, width=40, height=35, image=paper)
widgetPaper.place(x=145,y=10)

widgetS = Button(root, command=Scissors, width=40, height=35, image=scissors)
widgetS.place(x=245,y=10)

resultText = StringVar()
resultText.set("Go!")
widgetResult = Label(root, textvariable=resultText, width = 42)
widgetResult.place(x=0, y=100)

widgetE = Button(root, text='End Game', command=quit, width=30)
widgetE.place(x=50, y=220)

namelbl = Label(root, text="Credits:- Rohit Kavitake")
namelbl.place(x=180,y=270)

root.title('Rock, Paper, Scissors! game')
root.mainloop()