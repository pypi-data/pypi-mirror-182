import time
from tkinter import *
import tkinter.messagebox
import datetime
import os
import random
import turtle



class Operator():
    class Other():
        class PowerNumber():
            def Gui():
                W = Tk()
                W.title("Soustraction - 2023-2024yrs ")
                W.geometry("500x500")
                LET1 = Label(W, text="The First value").pack()
                talone = Entry(W)
                talone.pack()
                LET2 = Label(W, text="The second value").pack()
                taltwo = Entry(W)
                taltwo.pack()
                

                def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) ** int(taltwo.get()))

                ButtonSend = Button(W, text="Send and add '[T1 ** T2]' VALUE",command=MessRes)
                ButtonSend.pack()


                W.mainloop()
            def Terminal():
                ValueN1 = int(input("Enter first arguments(value) : "))
                ValueN2 = int(input("Enter second arguments(value) : "))
                def Play(x,y):
                    return x ** y
                QSD = input("See the result : ")
                if QSD == "yes" or QSD == "Yes":
                    print(Play(ValueN1, ValueN2))
    class Adition():
        def Gui():
            W = Tk()
            W.title("Addition - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                tkinter.messagebox.showinfo("Results", int(talone.get()) + int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 + T2]' VALUE",command=MessRes)
            ButtonSend.pack()


                    

            



            



            

           



            W.mainloop()
            def GuiError():
                import tkinter.messagebox
                tkinter.messageboxmessagebox.showerror(
                        "Error in the program", 
                        "The error is to find, but the rules dont be accept if you dont write the good code or you dont use the good number (exemple: you use charcter and not number...)")
                W = Tk()
                W.title("Error")



                W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x + y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Soustraction():
        def Gui():
            W = Tk()
            W.title("Soustraction - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                tkinter.messagebox.showinfo("Results", int(talone.get()) - int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 - T2]' VALUE",command=MessRes)
            ButtonSend.pack()


            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x - y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Multiplication():
        def Gui():
            W = Tk()
            W.title("Multiplication - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) * int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 * T2]' VALUE",command=MessRes)
            ButtonSend.pack()

            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x * y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Division():
        def Gui():
            W = Tk()
            W.title("Division - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def dATA_():
                NW = Tk()
                NW.title("Result of dATA_TYPES")
                NW.geometry("500x300")
            def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) / int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 / T2]' VALUE",command=MessRes)
            ButtonSend.pack()


            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x / y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))

class ProblemRandom():
    class Adition():
        def Gui():
            None
        def Terminal():
            None
    class Soustraction():
        def Gui():
            None
        def Terminal():
            None
    class Multiplication():
        def Gui():
            None
        def Terminal():
            None
    class Division():
        def Gui():
            None
        def Terminal():
            None



class DrawerPos():
    class DrawerLibrary():
        class Shape():
            def Circle(WindowName, Size, TextColor, Speed, waitTime, BgColor):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                t.color(TextColor)
                t.speed(Speed)
                turtle.bgcolor(BgColor)
                time.sleep(waitTime)
                t.circle(Size)

                turtle.done()
            def Rectangle(Color, speed, BackgroundColor, WindowName):
                print("Will next Update 0.0.3")
            def Square(Color, speed, BackgroundColor, WindowName):
                print("Will next Update 0.0.3")
            def Rombhus(Color, speed, BackgroundColor, WindowName):
                print("Will next Update 0.0.3")
            def Pentagone(Color, speed, BackgroundColor, WindowName):
                print("Will next Update 0.0.3")
            def Hexagone(Color, speed, BackgroundColor, WindowName):
                print("Will next Update 0.0.3")
            def Octogone(Line,Color, speed, BackgroundColor, WindowName):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                LEFTVAMUE = 90/2
                t.color(Color)
                t.speed(speed)
                turtle.bgcolor(BackgroundColor)
                t.forward(Line/2)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line/2)


                turtle.done()
            def Triangle(SizeLine ,leftFirst, LeftOf2line,Color, speed, BackgroundColor, WindowName):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                t.color(Color)
                t.speed(speed)
                turtle.bgcolor(BackgroundColor)
                t.forward(SizeLine/2)
                t.left(leftFirst)
                t.forward(SizeLine)
                t.left(LeftOf2line)
                t.forward(SizeLine)
                t.left(LeftOf2line)
                t.forward(SizeLine/2)

                

                turtle.done()
 
        class PersonOrPeople():
            None 