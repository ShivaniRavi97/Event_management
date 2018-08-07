
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


class Menu_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here(Buttons for linking to different frames)
		button1 = tk.Button(self, text = "Add Events",command = lambda: controller.show_frame("Event_page"))
		button2 = tk.Button(self, text = "Add Participants",command = lambda: controller.show_frame("Add_participants_page"))
		button3 = tk.Button(self, text = "See Participants",command = lambda: controller.show_frame("See_participants_page"))
		button1.grid(row =0, column = 0, padx=10, pady =10)
		button2.grid(row = 0, column = 3, padx=10, pady =10)
		button3.grid(row = 1,column =1,columnspan=2,padx=10, pady =10 )

class Event_page(tk.Frame):

	def add_event(self):
		self.ename = self.name_text.get("1.0","end-1c")
		self.eprice=self.price_text.get("1.0","end-1c")
		print(self.ename, self.eprice)
		with open('events.csv','a',newline="") as f:
			wr=csv.writer(f, dialect='excel')
			wr.writerow([self.ename,self.eprice])

	


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller  = controller
		#Add code here for Add Event Frame
		self.event_name = tk.Label(self,text = " Event Name")
		self.price = tk.Label(self,text = "Price")
		self.name_text = tk.Text(self, height=1,width=30)
		self.price_text = tk.Text(self, height=1,width=30)
		self.back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		self.event_name.grid(row=0,column =0)
		self.name_text.grid(row= 0, column = 1, columnspan = 3)
		self.price.grid(row=1,column =0)
		self.price_text.grid(row= 1, column = 1, columnspan = 3)
		self.back.grid(row=3,column = 0)
		# self.ename = self.name_text.get("1.0","end-1c")
		# self.eprice=self.price_text.get("1.0","end-1c")
		self.submit = tk.Button(self, text = "Submit", command =self.add_event).grid(row=2, column=0)
		#print(self.ename, self.eprice)

		

		


	
	

		# Add code for adding event to events.csv
		
class Add_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here for Add Participant Frame
		participant_name = tk.Label(self,text = "Participant Name")
		college_name = tk.Label(self, text = "College name")
		participant_name_text = tk.Entry(self)
		college_name_text = tk.Entry(self)
		participant_name.grid(row =0, column =0,padx=10, pady =10)
		participant_name_text .grid(row = 0, column =1, columnspan =2,padx=10, pady =10)
		college_name.grid(row =1, column =0, padx=10, pady =10) 
		college_name_text.grid(row =1, column =1,columnspan =2,padx=10, pady =10)
		back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"), padx=10, pady =10)
		back.grid(row=2,column = 2,padx=10, pady =10)



	def add_participant(self):
		pass
		# Add code for adding event to participants.csv


class See_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		#Add code here for View Paricipant Frame
		m = tk.Text(self,width=20,height=10)
		back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		m.grid(padx=10, pady =10)
		back.grid(padx=10, pady =10)

	def view_participant(self):
		pass
		# Add code for displaying from participants.csv
if __name__ =="__main__":
	a = EventManagement()
	a.mainloop()

