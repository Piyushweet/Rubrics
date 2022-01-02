from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import matplotlib.pyplot as plt
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkvideo import tkvideo
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from PIL import ImageSequence

import pygame
def main():
    root=Tk()
    app=Dic_Window(root)
    root.mainloop()


class Dic_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Roll_Dice")
        self.root.geometry("1550x800+0+0")
        video_label = Label(root)
        video_label.pack()
        player = tkvideo("dice.mp4", video_label,loop = 1, size = (1080, 700))
        player.play()
        myname=Label(self.root,text="Developed By:KPA",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname.place(x=0,y=0)
        myname=Label(self.root,text="Monte Carlo Problem",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname.place(x=1290,y=0)
        btn_login=Button(text="Roll",borderwidth=3,relief=RAISED,command=self.d_w,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        btn_login.place(x=700,y=700,width=175,height=35)
    def d_w(self):
        self.new_window=Toplevel(self.root)
        pygame.mixer.init() 
        img=Image.open("Dice.gif")
        pygame.mixer.music.load("Sound.wav")
        pygame.mixer.music.play(loops=1)
        lb1=Label(root)
        lb1.place(x=0,y=0)  

        for img in ImageSequence.Iterator(img):
            img=ImageTk.PhotoImage(img)
            lb1.config(image=img)
            root.update()
        self.app=Dice_Window( self.new_window)

class Dice_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Roll_Dice2")
        self.root.geometry("1550x800+0+0")
        #btn_exit=Button(text="Exit",borderwidth=3,relief=RAISED,command=self.exi,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        #btn_exit.place(x=700,y=700,width=175,height=35)
        myname=Label(self.root,text="Developed By:KPA",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname.place(x=0,y=0)
        myname1=Label(self.root,text="Monte Carlo Problem",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname1.place(x=1290,y=0)
        frame=Frame(self.root,bg="grey")
        frame.place(x=700,y=100,width=520,height=400)
        frame1=Frame(self.root,bg="grey")
        frame1.place(x=50,y=100,width=520,height=240)
        myname2=Label(self.root,text="TABLE",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname2.place(x=240,y=60)
        myname3=Label(self.root,text="GRAPH",fg="black",bg="white",font=("times new roman",18,"bold"))
        myname3.place(x=920,y=60)
        #btn_login=Button(text="Roll",borderwidth=3,relief=RAISED,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        #btn_login.place(x=700,y=700,width=175,height=35)

        
        
        
        rd_table = ttk.Treeview(frame1)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 20, BOLD))
        style.configure("Treeview", font=(None, 16))
        rd_table['columns'] = ('S.No.','Dice_Score', 'Percantage_Odds')

        rd_table.column("#0", width=0,  stretch=NO)
        rd_table.column("S.No.",anchor=CENTER, width=100)
        rd_table.column("Dice_Score",anchor=CENTER, width=160)
        rd_table.column("Percantage_Odds",anchor=CENTER,width=240)
    
        rd_table.heading("#0",text="",anchor=CENTER)
        rd_table.heading("S.No.",text="S.No.",anchor=CENTER)
        rd_table.heading("Dice_Score",text="Dice_Score",anchor=CENTER)
        rd_table.heading("Percantage_Odds",text="Percantage_Odds",anchor=CENTER)
        
        rd_table.pack()

        from random import randint
        import matplotlib.pyplot as plt
        outcome = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0} 
        res =10000

        for simulations in range(res):
            first_dice_roll = randint(1,6)
            second_dice_roll = randint(1,6)
            sum_dice = first_dice_roll + second_dice_roll
            outcome[sum_dice] += 1 
        
        m=1
       
        figure = Figure(figsize=(5, 5), dpi=100)
        ax = figure.add_subplot(111)
        
        for key in outcome.keys():
            z=outcome[key]/res*100
            
    
            rd_table.insert(parent='',index='end',text='',values=(m,key,z))
            m +=1
            lst=[key,z]
            print(lst)
            
            ax.scatter(key, z,s=20,c="green")
            #canvas.draw()
        
        canvas = FigureCanvasTkAgg(figure, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas.get_tk_widget().pack()


           
        

if __name__ == "__main__":
    root=Tk()
    app=Dic_Window(root)
    root.mainloop()

