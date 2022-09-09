import sqlite3

#connecting to database
conn = sqlite3.connect("Vacation2.db")

#creating a cursor
c = conn.cursor()

# ---------------------------------------------------------------------------
#create table Customer
c.execute('''CREATE TABLE Customer (
                    CustomerID integer NOT NULL PRIMARY KEY,
                    PassportNo text UNIQUE NOT NULL,
                    Address text,
                    Name text NOT NULL,
                    Budget integer,
                    Duration integer NOT NULL,
                    GroupCount integer NOT NULL);''')

# ----------------------------------------------------------------------------
#create table Hotel
c.execute('''CREATE TABLE Hotel (
                    HotelID text NOT NULL PRIMARY KEY,
                    HotelName text NOT NULL,
                    HotelRating integer,
                    HotelAddress text NOT NULL);''')

#create table Room
c.execute('''CREATE TABLE Room (
                    HotelID text,
                    RoomNo integer NOT NULL PRIMARY KEY,
                    RoomType text,
                    BedType text,
                    RoomPrice integer NOT NULL,
                    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID));''')

#create table HotelFacilities 
c.execute('''CREATE TABLE HotelFacilities (
                    HotelID text,
                    FreeParking numeric, 
                    SwimmingPool numeric, 
                    FitnessCentre numeric,
                    PetAllowed numeric,
                    BreakfastIncluded numeric,
                    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID));''')

# ----------------------------------------------------------------------------
#create table Airplane 
c.execute('''CREATE TABLE Airplane (
                    AirplaneID text NOT NULL PRIMARY KEY,
                    Capacity integer,
                    ModelName text);''')

#create table Flight 
c.execute('''CREATE TABLE Flight (
                    FlightNo text NOT NULL PRIMARY KEY,
                    AirplaneID text,
                    Origin text NOT NULL,
                    Destination text NOT NULL,
                    ArrivalDateTime integer NOT NULL,
                    DepDateTime integer NOT NULL,
                    Layover numeric NOT NULL,
                    Service text,
                    FOREIGN KEY (AirplaneID) REFERENCES Airplane(AirplaneID));''')

#create table Seat 
c.execute('''CREATE TABLE Seat (
                    FlightNo text,
                    SeatNo text NOT NULL PRIMARY KEY,
                    SeatPrice integer NOT NULL,
                    SeatClass text,
                    FOREIGN KEY (FlightNo) REFERENCES Flight(FlightNo));''')

# ----------------------------------------------------------------------------
#create table Travel Package
c.execute('''CREATE TABLE TravelPackage (
                    PackageID text NOT NULL PRIMARY KEY,
                    PackageName text,
                    FlightNo text,
                    HotelID text,
                    FOREIGN KEY (FlightNo) REFERENCES Flight(FlightNo),
                    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID));''')

# ----------------------------------------------------------------------------
#create table Payment
c.execute('''CREATE TABLE Payment (
                     PaymentID text NOT NULL PRIMARY KEY,
                     RoomPrice integer,
                     SeatPrice integer, 
                     PaymentDateTime numeric NOT NULL,
                     CreditCardDetails text NOT NULL,
                     TransactionAmount integer NOT NULL,
                     PackageID integer,
                     FOREIGN KEY (RoomPrice) REFERENCES Room(RoomPrice),
                     FOREIGN KEY (SeatPrice) REFERENCES Seat(SeatPrice),
                     FOREIGN KEY (PackageID) REFERENCES TravelPackage(PackageID));''')
















