import tkinter as tk
import csv



class EventManagement(tk.Tk):
	def __init__(self,*args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side = "top", fill ="both", expand= True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		#Add code here
		self.frames = {}
		for F in (Menu_page, Event_page, Add_participants_page,See_participants_page):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row =0, column = 0, sticky = 'nsew')

		self.show_frame("Menu_page")
	def show_frame(self, page_name):
		# Add code for displaying Corresponding Frame.
		frame = self.frames[page_name]
		frame.tkraise()

class Add_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here for Add Participant Frame
		participant_name = tk.Label(self,text = "Participant Name")
		college_name = tk.Label(self, text = "College name")
		participant_name_text = tk.Entry(self)
		college_name_text = tk.Entry(self)
		participant_name.grid(row =0, column =0)
		participant_name_text .grid(row = 0, column =1, columnspan =2)
		college_name.grid(row =1, column =0) 
		college_name_text.grid(row =1, column =1,columnspan =2)
		back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		back.grid(row=2,column = 0)



	def add_participant(self):
		pass
		# Add code for adding event to participants.csv
class Menu_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here(Buttons for linking to different frames)
		button1 = tk.Button(self, text = "Add Events",command = lambda: controller.show_frame("Event_page"))
		button2 = tk.Button(self, text = "Add Participants",command = lambda: controller.show_frame("Add_participants_page"))
		button3 = tk.Button(self, text = "See Participants",command = lambda: controller.show_frame("See_participants_page"))
		button1.grid(row =0, column = 0)
		button2.grid(row = 0, column = 2)
		button3.grid(row = 1,column =1,columnspan=2)

class Event_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller  = controller
		#Add code here for Add Event Frame
		event_name = tk.Label(self,text = " Event Name")
		price = tk.Label(self,text = "Price")
		name_text = tk.Entry(self)
		price_text = tk.Entry(self)
		back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		event_name.grid(row=0,column =0)
		name_text.grid(row= 0, column = 1, columnspan = 3)
		price.grid(row=1,column =0)
		price_text.grid(row= 1, column = 1, columnspan = 3)
		back.grid(row=2,column = 0)


	
	def add_event(self):
		
		# Add code for adding event to events.csv
		pass



class See_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here for View Paricipant Frame
		m = tk.Text(self,width=20,height=10)
		back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		m.pack()
		back.pack()

	def view_participant(self):
		pass
		# Add code for displaying from participants.csv
if __name__ =="__main__":
	a = EventManagement()
	a.mainloop()


	import tkinter as tk
import csv
root = tk.Tk()
# def main():
# 	f2 = tk.Frame(root)
# 	add = tk.Button(f2, text = " Add Events ",command = event )
# 	participants = tk.Button(f2, text = "Add Participants")
# 	view = tk.Button(f2, text = "View Participants")

# 	add.grid(row = 0, column = 0, padx= 10, pady = 10)
# 	participants.grid(row = 0, column = 2, padx= 10, pady = 10)
# 	view.grid(row = 1, column = 1, padx= 10, pady = 10)
# 	f2.grid(row = 0, column = 0)
# 	root.mainloop()

# def event():
# 	f1 = tk.Frame(root)
# 	t1 = tk.Entry(f1)
# 	t2 = tk.Entry(f1)
# 	l1 = tk.Label(f1, text = "Name")
# 	l2 =tk.Label(f1, text = "Price")
# 	b1 = tk.Button(f1, text = "Back", command=main)
# 	name = t1.get()
# 	price = t2.get()
# 	t1.grid(row = 0,column = 1, columnspan = 3 ,padx = 10, pady = 10 )
# 	t2.grid(row =1,column = 1 , columnspan = 3,padx = 10, pady = 10 )
# 	l1.grid(row = 0,column = 0 ,padx =10, pady = 10)
# 	l2.grid(row = 1 ,column = 0,padx =10 , pady = 10 )
# 	f1.grid(row = 0, column = 0)
# 	b1.grid(row = 3, column = 1, columnspan = 2 ,padx = 10, pady = 10 )
# 	root.mainloop()
	

# main()
class EventManagement(tk.Tk):

	def __init__(self, parent, controller):
		tk.Tk.__init__(self,parent)
		#container = tk.Frame(self)
		tk.Frame.grid()
		#Add code here
	
	def show_frame(self, page_name):
		pass
		# Add code for displaying Corresponding Frame.

class Menu_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		add = tk.Button(self, text = " Add Events ",command = event )
		participants = tk.Button(self, text = "Add Participants")
		view = tk.Button(self, text = "View Participants")

		add.grid(row = 0, column = 0, padx= 10, pady = 10)
		participants.grid(row = 0, column = 2, padx= 10, pady = 10)
		view.grid(row = 1, column = 1, padx= 10, pady = 10)
		f2.grid(row = 0, column = 0)
		
			#Add code here(Buttons for linking to different frames)

class Event_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#Add code here for Add Event Frame
	
	def add_event(self):
		pass
		# Add code for adding event to events.csv

class Add_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#Add code here for Add Participant Frame

	def add_participant(self):
		pass
		# Add code for adding event to participants.csv

class See_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#Add code here for View Paricipant Frame

	def view_participant(self):
		pass
		# Add code for displaying from participants.csv



o1 =EventManagement()
o1.mainloop()