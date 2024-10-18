import tkinter as tk
from tkinter import *
from tkinter import ttk
def displayLabel():
	a=e1.get()
	l1.config(text=a)
def displayList():
	a=e1.get()
	if a:
		listbox.insert(tk.END, a)
		e1.delete(0,tk.END)
def displayTable():
	a=e1.get()
	if a:
		t.insert("",tk.END, values=(len(t.get_children())+1, a))
		e1.delete(0,tk.END)
		
root=Tk()
e1=Entry()
e1.pack()
b1=Button(root,text="ADD",command=displayTable)
b1.pack()
#l1=Label()
#l1.pack()
#listbox=Listbox()
#listbox.pack()
columns=("Index","Data")
t=tk.ttk.Treeview(root,columns=columns, show="headings")
t.heading("Index", text="Index")
t.heading("Data", text="Data")
t.pack()
root.mainloop()