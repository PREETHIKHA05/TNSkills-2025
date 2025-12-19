from flask import Flask, render_template
import csv
from database import create_tables
import sqlite3
db_name='vehicle.db'
app=Flask(__name__)
create_tables()
def parse_data():
    cleaned_rows=[]
    with open('driver_logs_raw.csv','r') as f:
        readerObject=list(csv.reader(f))[1:]
        for row in readerObject:
                    if not(row[3].isdigit()):
                         continue
                    if not(row[4].isdigit()):
                         continue
                    cleaned_rows.append(row)
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    for row in cleaned_rows:
        cur.execute('Insert into trip(VehicleID,StartDate,EndDate,DriverName,StartDate,DistanceKm) values(?,?,?,?,?,?)',(row[0],row[1],row[1],row[2],row[3],row[4]))
        conn.commit()
def populate_data():
     conn=sqlite3.connect(db_name)
     cur=conn.cursor()
     cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V1", "REG-001" , "Truck" , "2025-05-20" , 20000 , 10000 ))
     cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_001" , "REG-101" , "Van" , "2025-10-01" , 50400 , 40400))
     cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_002" , "REG-102" , "Car" , "2025-11-15" , 12050 , 10000 ))
     cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_003" , "REG-103" , "Van" , "2025-08-20" , 8200 , 2000 ))
     cur.execute('insert into trip values( ?, ? , ?, ? ,?,?)',( 1 , "V1" , "TestDriver" , "2025-12-20" , "2025-12-30 ",500))
     conn.commit()

def show_tables():
     conn=sqlite3.connect(db_name)
     cur=conn.cursor()
     cur.execute('select * from vehicles')
     data=cur.fetchall()
     print(data)
     cur.execute('select * from trip')
     data=cur.fetchall()
     print(data)


@app.route('/')
@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)