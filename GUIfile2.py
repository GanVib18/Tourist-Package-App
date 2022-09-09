import tkinter as tk 
from tkinter import *
import PIL
from PIL import ImageTk 
import sqlite3

#initialize our app
root = tk.Tk()
root.title("Tourist Package App")

#================================================================
#================================================================
#Connect to database
connection = sqlite3.connect(r"C:\354project\Vacation2.db")
c = connection.cursor()

# ----------------------------------------------------------------------------
#insert rows into table Customer
c.execute('''INSERT INTO  Customer(CustomerID, PassportNo, Address, Name, Budget, Duration, GroupCount)
             VALUES
                (1, 'R0123456','56D Golden Avenue Vancouver V5S 1G9','Jane Smith', 900, 2,1),
                (2, 'A1987654','1650 136th Street Surrey V1K 8C9', 'Anna Hart', 6000, 7, 2),
                (3, 'C2345678', '3901 Skyline Drive Burnaby V5C 0J2','Pearl Allen', 8000, 9, 5),
                (4, 'J9876543','4392 Toy Avenue Langley  L1V 1S8', 'Bella Baker' , 3500 , 3, 1),
                (5, 'M0928374', '5638 144 Ave Vancouver T5E 6A3', 'Nick Brown' , 7000, 6, 4);''')

# ----------------------------------------------------------------------------
#insert rows into table Hotel
c.execute('''INSERT INTO Hotel(HotelID, HotelName, HotelRating, HotelAddress)
             VALUES
                ('BK123', 'Ambassador Hotel', 4, 'Bangkok'),
                ('BK221', 'Siam Star Hotel', 4, 'Bangkok'),
                ('BK223', 'EasyLife Hotel', 2, 'Bangkok'),
                ('PA124', 'La Belle Ville', 2, 'Paris'),
                ('PA333', 'Four Seasons', 5, 'Paris'),
                ('ND125', 'The Leela Palace', 5, 'New Delhi'),
                ('ND555', 'Ambassador Hotel', 3, 'New Delhi');''')

#insert rows into table Room
c.execute('''INSERT INTO Room (HotelID, RoomNo, RoomType, BedType, RoomPrice)
             VALUES
                ('BK123', 002, 'Accessible Room', 'Studio', 50),
                ('BK123', 200, 'Standard Room', 'Queen', 38),
                ('BK221', 031, 'Accessible Room', 'Twin', 89),
                ('BK221', 290, 'Standard Room', 'Queen', 70),
                ('BK221', 111, 'Deluxe Room', 'King', 100),
                ('BK223', 119, 'Standard Room', 'Queen', 25),
                ('BK223', 100, 'Deluxe Room', 'King', 35),
                ('PA124', 087, 'Connecting Room', 'Holiday Twin', 149),
                ('PA124', 185, 'Standard Room', 'Queen', 197),
                ('PA333', 003, 'Connecting Room', 'Holiday Twin', 449),
                ('PA333', 181, 'Standard Room', 'Queen', 270),
                ('ND125', 049, 'Standard Room', 'Queen', 169),
                ('ND125', 222, 'Deluxe Room', 'King', 300),
                ('ND555', 006, 'Standard Room', 'Queen', 111),
                ('ND555', 228, 'Deluxe Room', 'King', 200);''')

#insert rows into table HotelFacilities
c.execute('''INSERT INTO HotelFacilities (HotelID, FreeParking, SwimmingPool, FitnessCentre, PetAllowed, BreakfastIncluded)
             VALUES
                ('BK123', 0, 0, 1, 0, 1),
                ('BK221', 1, 1, 1, 1, 1),
                ('BK223', 0, 0, 1, 0, 0),
                ('PA124', 0, 1, 1, 0, 1),
                ('PA333', 1, 1, 1, 0, 1),
                ('ND125', 1, 1, 1, 1, 1),
                ('ND555', 1, 1, 1, 0, 0);''')

# ----------------------------------------------------------------------------
#insert rows into table Airplane
c.execute('''INSERT INTO Airplane(AirplaneID, Capacity, ModelName)
             VALUES
                ('A350900', 320, 'Airbus A350-900'),
                ('FHZUAJ', 400, 'Airbus A220-300'),
                ('F8C35Y195', 600, 'Boeing 777');''')

#insert rows into table Flight
c.execute('''INSERT INTO Flight(FlightNo, AirplaneID, Origin, Destination, ArrivalDateTime, DepDateTime, Layover, Service)
             VALUES
                 ('TA2346', 'A350900', 'Seattle', 'Bangkok', "2022-09-04 11:00:00 UTC", "2022-09-15 13:00:00 UTC", 1, 'Food only'),
                 ('TA2347', 'A350900', 'Seattle', 'Bangkok', "2022-09-03 23:00:00 UTC", "2022-09-14 8:00:00 UTC", 1, 'Food and Drinks'),
                 ('TA2348', 'A350900', 'Seattle', 'Bangkok', "2022-08-23 18:00:00 UTC", "2022-08-24 3:00:00 UTC", 0, 'Food and Drinks'),
                 ('TA2349', 'A350900', 'Seattle', 'Bangkok', "2022-08-27 16:00:00 UTC", "2022-08-29 1:00:00 UTC", 1, 'Food only'),
                 ('TA2350', 'FHZUAJ', 'Seattle', 'Bangkok', "2022-09-11 20:00:00 UTC", "2022-09-12 7:00:00 UTC", 0, 'Food only'),
                 ('AF1122', 'FHZUAJ', 'Vancouver', 'Paris', "2022-10-07 7:20:00 UTC", "2022-10-07 18:00:00 UTC", 0, 'Food and Drinks'),
                 ('AF1123', 'FHZUAJ', 'Vancouver', 'Paris', "2022-10-10 7:20:00 UTC", "2022-10-11 18:00:00 UTC", 0, 'Food and Drinks'),
                 ('AI7890', 'F8C35Y195', 'Toronto', 'Delhi', "2022-08-12  22:00:00 UTC", "2022-08-13 20:00:00 UTC", 0, 'Food only'),
                 ('AI7891', 'A350900', 'Toronto', 'Delhi', "2022-11-09  22:00:00 UTC", "2022-11-11 3:00:00 UTC", 1, 'Food and drinks');''')

#insert rows into table Seat
c.execute('''INSERT INTO Seat(FlightNo, SeatNo, SeatPrice, SeatClass)
             VALUES 
                ('TA2346', '2B', 1300, 'Business'),
                ('TA2346', '30A', 700, 'Economy'),
                ('TA2347', '5A', 1350, 'Business'),
                ('TA2347', '31A', 750, 'Economy'),
                ('TA2348', '1C', 1200, 'Business'),
                ('TA2348', '19A', 550, 'Economy'),
                ('TA2349', '19E', 800, 'Economy'),
                ('TA2349', '19D', 780, 'Economy'),
                ('TA2350', '6F', 900, 'Business'),
                ('TA2350', '23A', 400, 'Economy'),
                ('TA2350', '16D', 450, 'Economy'),
                ('AF1122', '1A', 1500, 'Business'),
                ('AF1122', '20C', 600, 'Economy'),
                ('AF1123', '1B', 1500, 'Business'),
                ('AF1123', '22B', 600, 'Economy'),
                ('AI7890', '4A', 1400, 'Business'),
                ('AI7890', '17C', 800, 'Economy'),
                ('AI7891', '3A', 1499, 'Business'),
                ('AI7891', '27C', 899, 'Economy');''')


#Commit changes and close connection
connection.commit()
connection.close()

#================================================================
#================================================================


#================================================================
#Change Helper function

def change():
	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	record_id = CID_box.get()

	c.execute("""UPDATE Customer SET
		PassportNo = :bb,
		Address = :cc,
		Name = :dd,
		Budget = :ee,
		Duration = :ff,
		GroupCount = :gg

		WHERE CustomerID = :ooid""", 

		{
		'bb': PassportNo_editor.get(),
		'cc': Address_editor.get(),
		'dd': Name_editor.get(),
		'ee': Budget_editor.get(),
		'ff': Duration_editor.get(),
		'gg': GroupCount_editor.get(),

		'ooid': record_id
		}
		)

	#Commit changes and close connection
	connection.commit()
	connection.close()

	#Close Window when done
	editor.destroy()

#================================================================
#Update Helper Window

def update():
	global editor
	editor = tk.Tk()
	editor.title("Update A Record")

	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#query the database
	c.execute("SELECT * FROM Customer WHERE CustomerID =" + CID_box.get())
	records = c.fetchall()

	#set global
	global PassportNo_editor
	global Address_editor
	global Name_editor
	global Budget_editor
	global Duration_editor
	global GroupCount_editor

	#create text boxes
	PassportNo_editor = Entry(editor, width=30)
	PassportNo_editor.grid(row=1, column=1)
	Address_editor = Entry(editor, width=30)
	Address_editor.grid(row=2, column=1)
	Name_editor = Entry(editor, width=30)
	Name_editor.grid(row=3, column=1)
	Budget_editor = Entry(editor, width=30)
	Budget_editor.grid(row=4, column=1)
	Duration_editor = Entry(editor, width=30)
	Duration_editor.grid(row=5, column=1)	
	GroupCount_editor = Entry(editor, width=30)
	GroupCount_editor.grid(row=6, column=1)

	#create text box label
	PassportNo_label = Label(editor, text="Passport Number")
	PassportNo_label.grid(row=1,column=0)
	Address_label = Label(editor, text="Address")
	Address_label.grid(row=2,column=0)
	Name_label = Label(editor, text="Name")
	Name_label.grid(row=3,column=0)
	Budget_label = Label(editor, text="Budget")
	Budget_label.grid(row=4,column=0)
	Duration_label = Label(editor, text="Duration")
	Duration_label.grid(row=5,column=0)
	GroupCount_label = Label(editor, text="GroupCount")
	GroupCount_label.grid(row=6,column=0)

	#Loop through results
	for record in records:
		PassportNo_editor.insert(0, record[1])
		Address_editor.insert(0, record[2])
		Name_editor.insert(0, record[3])
		Budget_editor.insert(0, record[4])
		Duration_editor.insert(0, record[5])
		GroupCount_editor.insert(0, record[6])

	#create save button
	save_button = Button(editor, text = "SAVE CHANGES", command = change)
	save_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#Commit changes and close connection
	connection.commit()
	connection.close()

#================================================================
#Delete Helper function

def delete():
	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	c.execute("DELETE from Customer WHERE CustomerID = " + CID_box.get())

	#Commit changes and close connection
	connection.commit()
	connection.close()

#================================================================
#Submit Helper function

def submit():

	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#insert into table
	c.execute("INSERT INTO Customer VALUES (:a, :b, :c, :d, :e, :f, :g)",
			{
				'a' : CustomerID.get(),
				'b' : PassportNo.get(),
				'c' : Address.get(),
				'd' : Name.get(),
				'e' : Budget.get(),
				'f' : Duration.get(),
				'g' : GroupCount.get()
			}
		)

	#Commit changes and close connection
	connection.commit()
	connection.close()

	#Clear
	CustomerID.delete(0,END)
	PassportNo.delete(0,END)
	Address.delete(0,END)
	Name.delete(0,END)
	Budget.delete(0,END)
	#Duration.delete(0,END)
	#GroupCount.delete(0,END)

#================================================================
#Submit Helper function

def showone():	
	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#query the database
	c.execute("SELECT * FROM Customer WHERE CustomerID =" + CID_box.get())
	records = c.fetchall()
	#print(records)

	#show_records =''
	#for i in records:
	#	show_records += str(i[0]) + '  ' + str(i[1]) + '  ' + str(i[2]) + '  ' + str(i[3]) + '  ' + str(i[4]) + '  ' + str(i[5]) + '  ' + str(i[6]) + "\n"

	output_text = "CustomerID -> " + str(records[0][0]) + "\n" + "PassportNo -> " + str(records[0][1]) + "\n" + "Address -> " + str(records[0][2]) + "\n" + "Name -> " + str(records[0][3]) + "\n" + "Budget -> " + str(records[0][4]) + "\n" + "Duration -> " + str(records[0][5]) + "\n" + "GroupCount -> " + str(records[0][6])
	#output_text = records

	query_label = Label(root, text = output_text)
	query_label.grid(row=14, column=0, columnspan=2)

	#Commit changes and close connection
	connection.commit()
	connection.close()

#================================================================
#Adding Widgets 

global Duration
global GroupCount

#create text boxes
CustomerID = Entry(root, width=30)
CustomerID.grid(row=0, column=1, padx=20, pady=(10,0))
PassportNo = Entry(root, width=30)
PassportNo.grid(row=1, column=1)
Address = Entry(root, width=30)
Address.grid(row=2, column=1)
Name = Entry(root, width=30)
Name.grid(row=3, column=1)
Budget = Entry(root, width=30)
Budget.grid(row=4, column=1)
Duration = Entry(root, width=30)
Duration.grid(row=5, column=1)	
GroupCount = Entry(root, width=30)
GroupCount.grid(row=6, column=1)

CID_box = Entry(root, width=30)
CID_box.grid(row=10,column=1, pady=5)

#create text box label
CustomerID_label = Label(root, text="Customer ID")
CustomerID_label.grid(row=0,column=0, pady=(10,0))
PassportNo_label = Label(root, text="Passport Number")
PassportNo_label.grid(row=1,column=0)
Address_label = Label(root, text="Address")
Address_label.grid(row=2,column=0)
Name_label = Label(root, text="Name")
Name_label.grid(row=3,column=0)
Budget_label = Label(root, text="Budget")
Budget_label.grid(row=4,column=0)
Duration_label = Label(root, text="Duration")
Duration_label.grid(row=5,column=0)
GroupCount_label = Label(root, text="GroupCount")
GroupCount_label.grid(row=6,column=0)

CID_label = Label(root, text="Enter your Customer ID")
CID_label.grid(row=10,column=0, pady=5)


#create submit button
submit_button = Button(root, text = "ADD RECORD", command = submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create a query button
query_button = Button(root, text = "SHOW RECORD", command = showone)
query_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create a Delete button
delete_button = Button(root, text = "DELETE RECORD", command = delete)
delete_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create an Update button
Update_button = Button(root, text = "UPDATE RECORD", command = update)
Update_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#================================================================
#================================================================
#================================================================
#================================================================
#================================================================

#================================================================
# save flight_cmd helper function

def save_flight_cmd():
	flight_oid_no = str(Row_ID.get())

	length = len(flight_records)

	global save_flight_no 
	global save_seat_no
	global save_seat_price

	save_flight_no = ''
	save_seat_no = ''
	save_seat_price = ''

	for i in (flight_records):
		if (flight_oid_no == str(i[0])):
			save_flight_no = str(i[1])
			save_seat_no = str(i[8])
			save_seat_price = int(str(i[9]))
			break

	#Close Window when done
	flights_window.destroy()


#================================================================
# show flights helper function
def show_flights():
	global flights_window
	flights_window = tk.Tk()
	flights_window.title("Flights")

	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#Aggregation Query 
	c.execute("""SELECT COUNT(Flight.FlightNo)
				FROM Flight
				INNER JOIN Seat ON Seat.FlightNo=Flight.FlightNo
				WHERE Flight.Origin=:xx AND Flight.Destination=:yy AND Seat.SeatClass=:zz;""", 
				{
				'xx': Origin.get(),
				'yy': Destination.get(),
				'zz': SeatClass.get()
				}
				)

	agg_var = c.fetchall()
	agg_text = "There are " + str(agg_var[0][0]) + " possible flight options."

	Agg_label = Label(flights_window, text = agg_text)
	Agg_label.grid(row=0, column=0, columnspan=5, pady=10)

	#query the database
	c.execute("""SELECT 
      ROW_NUMBER() OVER (ORDER BY (SELECT 1)) AS RowNo,
		Flight.FlightNo,
		Flight.Origin,
		Flight.Destination, 
		Flight.ArrivalDateTime,
		Flight.DepDateTime,
		Flight.Layover, 
		Flight.Service,
		Seat.SeatNo,
		Seat.SeatPrice, 
		Seat.SeatClass
		FROM Flight
		INNER JOIN Seat ON Seat.FlightNo=Flight.FlightNo
		WHERE Flight.Origin=:xx AND Flight.Destination=:yy AND Seat.SeatClass=:zz;""", 
		{
		'xx': Origin.get(),
		'yy': Destination.get(),
		'zz': SeatClass.get()
		}
		)

	global flight_records
	
	flight_records = c.fetchall()
	#print(records)

	sample_text =  "\t        RowNo" + "     " + "FlightNo" + "         " + "Origin" + "          " + "Destination" + "       " + "ArrivalDateTime" + "                       " + "DepDateTime" + "                     " + "Layover" + "   " + "Service" + "     " + "SeatNo" + "     " + "SeatPrice" + "     " + "SeatClass\t" 

	query_label = Label(flights_window, text = sample_text)
	query_label.grid(row=1, column=0, columnspan=11, pady=10)

	show_records =''
	for i in flight_records:
		show_records += '\t ' +'          ' + str(i[0]) + '           ' + str(i[1]) + '           ' + str(i[2]) + '           ' + str(i[3]) + '           ' + str(i[4]) + '    ' + str(i[5]) + '      ' + str(i[6]) + '       ' + str(i[7]) + '          ' +  str(i[8]) + '            ' +  str(i[9]) + '           ' +  str(i[10]) +  "\n"

	#output_text = "CustomerID -> " + str(records[0][0]) + "\n" + "PassportNo -> " + str(records[0][1]) + "\n" + "Address -> " + str(records[0][2]) + "\n" + "Name -> " + str(records[0][3]) + "\n" + "Budget -> " + str(records[0][4]) + "\n" + "Duration -> " + str(records[0][5]) + "\n" + "GroupCount -> " + str(records[0][6])
	#output_text = records

	query_label = Label(flights_window, text = show_records)
	query_label.grid(row=2, column=0, columnspan=11)

	global Row_ID

	#create Row_ID
	Row_ID_Label = Label(flights_window, text = "Enter Row No")
	Row_ID_Label.grid(row=3, column=0, pady=10, padx=10)
	Row_ID = Entry(flights_window, width=30)
	Row_ID.grid(row=3, column=1, pady=10)

	#create save button
	save_flight_button = Button(flights_window, text = "SAVE FLIGHT AND SEAT", command = save_flight_cmd)
	save_flight_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#Commit changes and close connection
	connection.commit()
	connection.close()

#================================================================
# show hotels facilites helper function
def show_facilites():
	hotel_oid_no = str(Hotel_Row_ID.get())
	sample_list = []

	for i in (hotel_records):
		if (hotel_oid_no == str(i[0])):
			sample_list.append(int(str(i[9])))
			sample_list.append(int(str(i[10])))
			sample_list.append(int(str(i[11])))
			sample_list.append(int(str(i[12])))
			sample_list.append(int(str(i[13])))
			break

	facilites_text =''

	if (sample_list[0] == 1):
		facilites_text += 'This Hotel has Free Parking.\n'
	if (sample_list[1] == 1):
		facilites_text += 'This Hotel has Swimming Pool.\n'
	if (sample_list[2] == 1):
		facilites_text += 'This Hotel has Fitness Center.\n '
	if (sample_list[3] == 1):
		facilites_text += 'This Hotel has Pets are Allowed.\n '
	if (sample_list[4] == 1):
		facilites_text += 'This Hotel has Breakfast Included.'

	query_label = Label(hotels_window, text = facilites_text)
	query_label.grid(row=4, column=3, columnspan=5)

#================================================================
# save hotel_cmd helper function

def save_hotel_cmd():
	hotel_oid_no = str(Hotel_Row_ID.get())

	length = len(hotel_records)

	global save_hotel_no 
	global save_room_no
	global save_room_price

	save_hotel_no = ''
	save_room_no = ''
	save_room_price = ''

	for i in (hotel_records):
		if (hotel_oid_no == str(i[0])):
			save_hotel_no = str(i[1])
			save_room_no = str(i[5])
			save_room_price = int(str(i[8]))
			break

	#Close Window when done
	hotels_window.destroy()

#================================================================
# show hotels helper function
def show_hotels():
	global hotels_window
	hotels_window = tk.Tk()
	hotels_window.title("Hotels")

	sample_text_2 =  "\t     RowNo" + "     " + "HotelID" + "     " + "Hotel Name" + "         " + "Hotel Rating" + "          " + "Hotel City" + "       " + "Room Number" + "        " + "Room Type" + "     " + "Bed Type" + "   " + "Room Price\t" 

	query_label = Label(hotels_window, text = sample_text_2)
	query_label.grid(row=0, column=0, columnspan=7, pady=10)

	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#query the database
	c.execute("""SELECT 
      ROW_NUMBER() OVER (ORDER BY (SELECT 1)) AS RowNo,
		Hotel.HotelID, 
		Hotel.HotelName,
		Hotel.HotelRating, 
		Hotel.HotelAddress,
		Room.RoomNo, 
		Room.RoomType,
		Room.BedType, 
		Room.RoomPrice,
		HotelFacilities.FreeParking, 
		HotelFacilities.SwimmingPool, 
		HotelFacilities.FitnessCentre, 
		HotelFacilities.PetAllowed,
		HotelFacilities.BreakfastIncluded
		FROM Hotel
		INNER JOIN Room ON Room.HotelID = Hotel.HotelID
		INNER JOIN HotelFacilities ON HotelFacilities.HotelID = Hotel.HotelID
		WHERE HotelAddress = :dest_var AND HotelRating = :yyy
		ORDER BY Room.RoomPrice ASC;""", 
		{
		'dest_var': Destination.get(),
		'yyy': HotelRating.get()
		}
		)

	global hotel_records
	
	hotel_records = c.fetchall()
	#print(records)

	show_hotel_records =''
	for i in hotel_records:
		show_hotel_records +=  str(i[0]) + '             ' + str(i[1]) + '               ' + str(i[2]) + '      ' + str(i[3]) + '           ' + str(i[4]) + '               ' + str(i[5]) + '                     ' + str(i[6]) + '       ' + str(i[7]) + '       ' +  str(i[8]) + "\n"

	query_label = Label(hotels_window, text = show_hotel_records)
	query_label.grid(row=1, column=0, columnspan=7)

	global Hotel_Row_ID

	c.execute("""
		SELECT MAX(x.avg)
		FROM ( SELECT AVG(Room.RoomPrice) as avg
					FROM Room
					LEFT JOIN Hotel ON Room.HotelID = Hotel.HotelID
					WHERE HotelAddress = :dest_var AND HotelRating = :yyy
					GROUP BY Room.HotelID)x;""", 
		{
		'dest_var': Destination.get(),
		'yyy': HotelRating.get()
		}
		)

	nested_agg_var = c.fetchall()

	nested_agg_text = "The most expensive room (on average) will cost ->"

	nested_agg_label = Label(hotels_window, text = nested_agg_text)
	nested_agg_label.grid(row=2, column=0)

	nested_agg_label_2 = Label(hotels_window, text = nested_agg_var)
	nested_agg_label_2.grid(row=2, column=1)


	#create Row_ID
	Hotel_Row_ID_Label = Label(hotels_window, text = "Enter Row No")
	Hotel_Row_ID_Label.grid(row=3, column=0, pady=10, padx=10)
	Hotel_Row_ID = Entry(hotels_window, width=30)
	Hotel_Row_ID.grid(row=3, column=1, pady=10)

	#create save button
	show_hotel_faci_button = Button(hotels_window, text = "SHOW HOTEL FACILITES", command = show_facilites)
	show_hotel_faci_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#create save button
	save_hotel_button = Button(hotels_window, text = "SAVE HOTEL AND ROOM", command = save_hotel_cmd)
	save_hotel_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#Commit changes and close connection
	connection.commit()
	connection.close()

#================================================================
# make_payment_function button
def make_payment_function():
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#insert into table
	c.execute("INSERT INTO Payment VALUES (:a, :b, :c, :d , :e, :f, :g)",
			{
				'a' : CID_box.get(),
				'b' : int(str(save_room_price)),
				'c' : int(str(save_seat_price)),
				'd' : Date_Time_box.get(),
				'e' : Credit_Card_box.get(),
				'f' : transaction_amt,
				'g' : PackageID.get()
			}
		)

	root.destroy()
	win2.destroy()
	win3.destroy()


	#Commit changes and close connection
	connection.commit()
	connection.close()

#==========================================================================
#division_query_func helper

def division_query_func():
	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	c.execute("""
		SELECT DISTINCT C.Name
		FROM Customer C
		WHERE C.Name NOT IN(
				SELECT C2.Name
				FROM Customer C2
				INNER JOIN TravelPackage TP ON TP.PackageID = C2.CustomerID
		);""")

	show_div_records = c.fetchall()

	xyz_label = Label(win3, text=show_div_records)
	xyz_label.grid(row=11,column=0)

#===========================================================================
#window 3 main
def payment_win():

	#Connect to database
	connection = sqlite3.connect(r"C:\354project\Vacation2.db")
	c = connection.cursor()

	#insert into table
	c.execute("INSERT INTO TravelPackage VALUES (:a, :b, :c, :d )",
			{
				'a' : PackageID.get(),
				'b' : Package_Name.get(),
				'c' : save_flight_no,
				'd' : save_hotel_no
			}
		)


	global win3
	win3 = tk.Tk()
	win3.title("Payment")

	#adding widgets
	PaymentID_label = Label(win3, text="Payment ID -> ")
	PaymentID_label.grid(row=0,column=0, pady=(10,0))
	PaymentID_val = Label(win3, text=CID_box.get())
	PaymentID_val.grid(row=0,column=1, pady=(10,0))

	RoomPrice_label = Label(win3, text="Room Price -> ")
	RoomPrice_label.grid(row=1,column=0)
	RoomPrice_val = Label(win3, text=save_room_price)
	RoomPrice_val.grid(row=1,column=1)

	SeatPrice_label = Label(win3, text="Seat Price -> ")
	SeatPrice_label.grid(row=2,column=0)
	SeatPrice_val = Label(win3, text=save_seat_price)
	SeatPrice_val.grid(row=2,column=1)

	global transaction_amt 
	transaction_amt = (save_seat_price * int(GroupCount.get()) ) + ( int(Duration.get()) * save_room_price ) 

	Netamt_label = Label(win3, text="Net Transaction Amount -> ")
	Netamt_label.grid(row=3,column=0)
	Netamt_val = Label(win3, text=transaction_amt)
	Netamt_val.grid(row=3,column=1)

	#linebreak
	Next_label_2 = Label(win3, text="================================================")
	Next_label_2.grid(row=4,column=0, columnspan=2)

	global Credit_Card_box
	global Date_Time_box

	#create Credit_Card Details
	Credit_Card_label = Label(win3, text="Enter your Credit Card Deatils ->")
	Credit_Card_label.grid(row=5,column=0)
	Credit_Card_box = Entry(win3, width=30)
	Credit_Card_box.grid(row=5, column=1, padx=20)

	#create Credit_Card Details
	Date_Time_label = Label(win3, text="Enter the current Date/Time ->")
	Date_Time_label.grid(row=6,column=0)
	Date_Time_box = Entry(win3, width=30)
	Date_Time_box.grid(row=6, column=1, padx=20)

	#create flight button
	make_payment_button = Button(win3, text = "MAKE PAYMENT", command = make_payment_function)
	make_payment_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#linebreak
	Next_label_2 = Label(win3, text="================================================")
	Next_label_2.grid(row=8,column=0, columnspan=2)

	#create flight button
	make_payment_button = Button(win3, text = "FIND NAMES OF CUSTOMERS WHO HAVEN'T BOOKED ANY TRAVEL PACKAGES", command = division_query_func)
	make_payment_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#linebreak
	Next_label_2 = Label(win3, text="================================================")
	Next_label_2.grid(row=15,column=0, columnspan=2)

	#Commit changes and close connection
	connection.commit()
	connection.close()


#================================================================
#================================================================

#window 2 main
def window2():
	global win2
	win2 = tk.Tk()
	win2.title("Travel Package")

	global PackageID
	global Package_Name

	#adding widgets
	PackageID_label = Label(win2, text="Package ID")
	PackageID_label.grid(row=0,column=0, pady=(10,0))
	PackageID = Entry(win2, width=30)
	PackageID.grid(row=0, column=1, padx=20, pady=(10,0))

	Package_Name_label = Label(win2, text="Package Name")
	Package_Name_label.grid(row=1,column=0)
	Package_Name = Entry(win2, width=30)
	Package_Name.grid(row=1, column=1, padx=20)

	#linebreak
	Next_label_2 = Label(win2, text="================================================")
	Next_label_2.grid(row=2,column=0, columnspan=2)

	#setting global variables
	global Origin
	global Destination
	global SeatClass
	global HotelRating

	Origin_label = Label(win2, text="Enter your origin")
	Origin_label.grid(row=3,column=0, pady=(5,0))
	Origin = Entry(win2, width=30)
	Origin.grid(row=3, column=1, padx=20, pady=(5,0))

	Destination_label = Label(win2, text="Enter your destination")
	Destination_label.grid(row=4,column=0)
	Destination = Entry(win2, width=30)
	Destination.grid(row=4, column=1, padx=20)

	SeatClass_label = Label(win2, text="Enter your preferred Seat Class")
	SeatClass_label.grid(row=5,column=0)
	SeatClass = Entry(win2, width=30)
	SeatClass.grid(row=5, column=1, padx=20)


	#create flight button
	flight_button = Button(win2, text = "SHOW FLIGHTS", command = show_flights)
	flight_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#linebreak
	Next_label_2 = Label(win2, text="================================================")
	Next_label_2.grid(row=7,column=0, columnspan=2)

	HotelRating_label = Label(win2, text="Enter your preferred Hotel Rating")
	HotelRating_label.grid(row=8,column=0)
	HotelRating = Entry(win2, width=30)
	HotelRating.grid(row=8, column=1, padx=20)

	#create hotel button
	hotel_button = Button(win2, text = "SHOW HOTELS", command = show_hotels)
	hotel_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

	#linebreak
	Next_label_2 = Label(win2, text="================================================")
	Next_label_2.grid(row=10,column=0, columnspan=2)

	#create hotel button
	hotel_button = Button(win2, text = "SAVE TRAVEL PACKAGE AND PROCEED TO PAYMENT", command = payment_win)
	hotel_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



#================================================================
#================================================================
#================================================================
#================================================================

#create a next label
Next_label = Label(root, text="================================================")
Next_label.grid(row=16,column=0, columnspan=2, pady=5)

#create a next button
Next_button = Button(root, text = "BUILD YOUR TRAVEL PACKAGE", command = window2)
Next_button.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#================================================================
#================================================================
#run app
root.mainloop()


