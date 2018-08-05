import csv
 class event_names:
 	def add_event():
 		event_name=t1.get()
 		price=t2.get()
 		with open('events.csv','a',newline="") as f:
 			wr=csv.writer(f, dialect='excel')
 			wr.writerow([event_name,price])


 				
