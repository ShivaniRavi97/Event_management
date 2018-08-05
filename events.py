import tkinter as tk
import csv
root = tk.Tk()
def main():
	f2 = tk.Frame(root)
	add = tk.Button(f2, text = " Add Events ",command = event )
	participants = tk.Button(f2, text = "Add Participants")
	view = tk.Button(f2, text = "View Participants")

	add.grid(row = 0, column = 0, padx= 10, pady = 10)
	participants.grid(row = 0, column = 2, padx= 10, pady = 10)
	view.grid(row = 1, column = 1, padx= 10, pady = 10)
	f2.grid(row = 0, column = 0)
	root.mainloop()

def event():
	f1 = tk.Frame(root)
	t1 = tk.Entry(f1)
	t2 = tk.Entry(f1)
	l1 = tk.Label(f1, text = "Name")
	l2 =tk.Label(f1, text = "Price")
	b1 = tk.Button(f1, text = "Back", command="main")
	name = t1.get()
	price = t2.get()
	t1.grid(row = 0,column = 1, columnspan = 3 ,padx = 10, pady = 10 )
	t2.grid(row =1,column = 1 , columnspan = 3,padx = 10, pady = 10 )
	l1.grid(row = 0,column = 0 ,padx =10, pady = 10)
	l2.grid(row = 1 ,column = 0,padx =10 , pady = 10 )
	f1.grid(row = 1, column = 0)
	b1.grid(row = 3, column = 1, columnspan = 2 ,padx = 10, pady = 10 )
	root.mainloop()
	

main()