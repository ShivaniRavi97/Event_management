
import tkinter as tk
import csv



class EventManagement(tk.Tk):
	def __init__(self,*args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side = "top", fill ="both", expand= True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.geometry("390x200+10+10")
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
		button1 = tk.Button(self, text = "Add Events",command = lambda: controller.show_frame("Event_page"),padx=5)
		button2 = tk.Button(self, text = "Add Participants",command = lambda: controller.show_frame("Add_participants_page"))
		button3 = tk.Button(self, text = "See Participants",command = lambda: controller.show_frame("See_participants_page"))
		button1.grid(row =4, column = 0, padx=20, pady =20, sticky = 'nsew')
		button2.grid(row = 4, column = 3, padx=20, pady =20, sticky = 'nsew')
		button3.grid(row = 8,column =1,columnspan=2,padx=20, pady =20,sticky = 'nsew' )

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
		self.event_name.grid(row=0,column =0,padx=20, pady=20)
		self.name_text.grid(row= 0, column = 1, columnspan = 3,padx=20, pady=20)
		self.price.grid(row=1,column =0,padx=20, pady=20)
		self.price_text.grid(row= 1, column = 1, columnspan = 3,padx=20, pady=20)
		self.back.grid(row=2,column=0, padx=20, pady=20)
		self.submit = tk.Button(self, text = "Submit", command =self.add_event).grid(row=2, column=3,padx=20, pady=20)
		

		
		


	
	

		
		
class Add_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.participant_name = tk.Label(self,text = "Participant Name")
		self.college_name = tk.Label(self, text = "College name")
		self.select_label = tk.Label(self, text = "Select Event")
		self.participant_name_text = tk.Text(self, height=1, width=30)
		self.college_name_text = tk.Text(self, height=1, width=30)
		self.participant_name.grid(row =0, column =0,padx=10, pady =10)
		self.participant_name_text .grid(row = 0, column =1, columnspan =2,padx=10, pady =10)
		self.college_name.grid(row =1, column =0, padx=10, pady =10) 
		self.college_name_text.grid(row =1, column =1,columnspan =2,padx=10, pady =10)
		self.select_label.grid(row = 2,column = 0,padx=10,pady = 10)
		self.back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"),padx=5)
		self.back.grid(row=3,column = 0,padx=10, pady=15)
		self.submit = tk.Button(self, text = "Submit", command =self.add_participant).grid(row=3, column=2)
		with open('events.csv', 'r') as eventfile:
			r = csv.reader(eventfile)
			options = []
			for line in r:
				options.append(line[0])
		variable = tk.StringVar(self)
		variable.set(options[0])

		select = tk.OptionMenu(self, variable,*options).grid(row =2,column =1,padx=10,pady=10)


	def add_participant(self):
		
		# Add code for adding event to participants.csv
		self.ename = self.participant_name_text.get("1.0","end-1c")
		self.eprice=self.college_name_text.get("1.0","end-1c")
		print(self.ename, self.eprice)
		with open('participants.csv','a',newline="") as f:
			wr=csv.writer(f, dialect='excel')
			wr.writerow([self.ename, self.eprice])



		
				



class See_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.textbox = tk.Text(self,width=45,height=7)
		self.back = tk.Button(self, text="Back",command=lambda: controller.show_frame("Menu_page"))
		self.view = tk.Button(self, text = " View", command =self.view_participant).grid(row =0,column=0,padx=5,pady=5)
		self.textbox.grid(rowspan = 5,padx=10, pady =5)
		self.back.grid(row=7, padx=5, pady =5)

	def view_participant(self):
		with open("participants.csv","r") as myfile:

			rd=csv.reader(myfile)
			for line in rd :
				print(f"{line[0]} - {line[1]}")
				self.textbox.insert("0.0",f"{line[0]},{line[1]} \n")

		
if __name__ =="__main__":
	a = EventManagement()
	a.mainloop()

