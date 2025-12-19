from flask import Flask, render_template
import csv
from database import create_tables
import sqlite3
db_name='vehicle.db'
app=Flask(__name__)


def parse_data():
    cleaned_rows=[]
    with open('driver_logs_raw.csv','r') as f:
        readerObject=csv.DictReader(f)
        for row in readerObject:
                    try:
                        
                        row["Odometer_Reading"]=int(row["Odometer_Reading"])
                        row["Trip_Distance"]=int(row(["Trip_Distance"]))
                        cleaned_rows.append(row)
                    except:
                        print("Error")
                        continue
    print(cleaned_rows)
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    for row in cleaned_rows:
        cur.execute('Insert into trips(VehicleID,StartDate,EndDate,DriverName,StartDate,DistanceKm) values(?,?,?,?,?,?)',(row['VehicleID'],dt,dt,row['Driver'],row['Odometer_Reading'],row['Trip_Distance']))
    conn.commit()
parse_data()
def show_tables():
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    cur.execute('select * from trip')
    rows=cur.fetchall()
    print(rows)
show_tables()
@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)