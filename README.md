# Tourist Package App	

Our group proposed a travel package database that first inputs customer information. Based on the given information such as the customer id, passport number, name, address, budget and groupcount, the customer gets the opportunity to customize the travel packages based on their preferences.The software system checks for user choice and then queries the database for various available mediums to travel to that destination. Moreover, the system allows the user to book tickets to the destination for the desired date and timings. This gives our customers lots of flexibility and the option to choose what they want for themselves.

The travel package includes both the flight and accommodation. Customers can filter based on the hotel ratings along with addresses and choose a plan for themselves. Similarly they can choose their flights along with the seat class they would prefer in the airplane. 

In short, our database is designed in a way that it allows users to check various destinations and based on what they like they can choose accordingly. The database displays the destinations and an accommodation nearby can also be chosen by the system. As the system has all the hotels that are close to different destinations chosen, they can be further filtered based on rooms within and the preferred bed type.

The data flow of our schema could be presented in this manner:
Customer Login -> Aggregated Flight Component -> Aggregated Hotel Component -> Appended to Travel Package -> Payment Method

We used different queries including select, project, update, insert, delete to make our GUI interface for our vacation travel packages database. We have used SQLite to combine MySQL and python for writing the DDL and queries for the project. To make our project functional and running, we have looked at different videos and lecture notes to understand how to implement our code and queries. The format for my SQLite is a bit different than MySQL so we had to look into that as well. We have implemented our code in a way that there are a series of buttons and a query behind each button.

We have worked on removing redundant data so that when we run our queries, we get the data required without any extraneous information. We have tried to make our vacation travel package database efficient so that it processes information and fetches queries effectively.
	
The main advantage of our vacation travel package database is that it automates the manual booking process of vacations by single individuals and groups. The payment and customization process is easy and flexible to use. This saves time for our customers and it is more convenient for them to book their tour online instead of visiting the agency. Another advantage is the incorporated payment method that comes along with the database booking system.

Language: Python
DataBase: SQL (Python library SQLite)
GUI: Tkinter Library

Authors - 
Inayat Lakhani	
Romeesa Jabbar
Vibhuti Gandhi
