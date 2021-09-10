# create-database-inserting-data-and-retrive-data-using-python
import sqlite3  
#Connecting to sqlite 
conn = sqlite3.connect('example.db')  
#Creating a cursor object using the cursor() method 
cursor = conn.cursor()  
#Doping EMPLOYEE table if already exists. 
cursor.execute("DROP TABLE IF EXISTS MovieDetails")  
#Creating table as per requirement 
sql ='''CREATE TABLE MovieDetails(    Movie_Name CHAR(20) Primary Key,    Hero CHAR(20), Heroine char(20),    Year_of_release year,    Director_name char(20) )''' cursor.execute(sql) print("Table created successfully........")
#Inserting Values 
cursor.execute("""INSERT INTO MovieDetails (Movie_Name, Hero,Heroine,Year_of_release,Director_name) VALUES ("Bahubhali 1", "Prabhas","Anushka","2015","Rajamouli")""") cursor.execute("""INSERT INTO MovieDetails (Movie_Name, Hero,Heroine,Year_of_release,Director_name) VALUES ("Bahubhali 2", "Prabhas","Anushka","2017","Rajamouli")""") cursor.execute("""INSERT INTO MovieDetails (Movie_Name, Hero,Heroine,Year_of_release,Director_name) VALUES ("Saho", "Sradha","Anushka","2019","Sujith")""") cursor.execute("""INSERT INTO MovieDetails (Movie_Name, Hero,Heroine,Year_of_release,Director_name) VALUES ("Sarileru neekevvaru", "Mahesh Babu","Rashmika","2020","Anil Ravipudi")""") 
cursor.execute("""INSERT INTO MovieDetails (Movie_Name, Hero,Heroine,Year_of_release,Director_name) VALUES ("Majili", "Chaitanya","Samantha","2019","Siva Nirvana")""")  print("INsert Done") 
cursor.execute("SELECT * FROM MovieDetails  ")
print("Printing table data") 
# fetch all the matching rows 
result = cursor.fetchall()
for row in result:     
  print(row)   
# Commit your changes in the database 
conn.commit()  
#Closing the connection conn.close()
