from tkinter import *
import random
import matplotlib.pyplot as plt
top=Tk()
top.geometry("400x200")
r=""
o=u=0
k=[]
m=[]
def typemaster():
      global r
      tb1.configure(state="normal")
      data=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','p1', 'q1', 'emp1', 'emp2', 'emp3', 'emp4','p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
      p=random.choice(data)
      r=p
      l1.configure(text=str(p))
def com():
      global k,m,o,u
      t=str(tb1.get())
      if t==r:
            o=o+1
            k.append(o)
            l2.configure(text="click on START to get next word")
      else:
            o=o-1
            k.append(o)
            l2.configure(text="you are falied")
      u=u+1
      m.append(u)
      tb1.delete(0,END)
def graph():
      plt.bar(m,k)
      plt.show()         
b1=Button(top,text="START",command=typemaster)
b1.pack()
l1=Label(top,text="click on the start button")
l1.pack()
tb1=Entry(top,width=50)
tb1.pack()
b2=Button(top,text="GO",command=com)
b2.pack()
l2=Label(top,text="final output")
l2.pack()
b3=Button(top,text="graph",command=graph)
b3.pack()


