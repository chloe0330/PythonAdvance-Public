from cProfile import label
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("사칙 연산 프로그램")

def click1(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) + int(txt2) 
    label3.config(text = (txt1) + " + " + (txt2) + " = " + str(answer)) 
def click2(): 
    text1 = entry1.get()
    text2 = entry2.get()
    answer = int(text1) - int(text2)
    label3.config(text = (text1) + " - " + (text2) + " = " + str(answer))
def click3(): 
    text1 = entry1.get()
    text2 = entry2.get()
    answer = int(text1) * int(text2)
    label3.config(text = (text1) + " x " + (text2) + " = " + str(answer))
def click4(): 
    text1 = entry1.get()
    text2 = entry2.get()
    answer = int(text1) / int(text2)
    label3.config(text = (text1) + " / " + (text2) + " = " + str(answer))
