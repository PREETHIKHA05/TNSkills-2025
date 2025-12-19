from flask import Flask, render_template
import csv
from database import create_tables
import sqlite3
create_tables()
db_name='vehicle.db'
app=Flask(__name__)


def parse_data(file):
    cleaned_rows=[]
    with open(file,'r') as f:
        readerObject=csv.DictReader(f)
        for row in readerObject:
            try:
                row["Odometer_Reading"]=int(row["Odometer_Reading"])
                row["Trip_Distance"]=int(row(["Trip_Distance"]))
                cleaned_rows.append(row)
            except:
                continue
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    for row in cleaned_rows:
        cur.execute('Insert into trips(VehicleID,DriverName,StartDate,DistanceKm) values(?,?,?,?)',(row['VehicleID'],row['Driver'],row['Odometer_Reading'],row['Trip_Distance']))

@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)