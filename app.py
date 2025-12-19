from flask import Flask, render_template
import csv
from database import create_tables
import sqlite3
db_name='vehicle.db'
app=Flask(__name__)


def parse_data():
    cleaned_rows=[]
    with open('driver_logs.csv','r') as f:
        readerObject=csv.DictReader(f)
        for row in readerObject:
            try:
                date=row["Date"].strip()
                if '/' in date:
                    correct_date=date.split('/')
                if '-' in date:
                    correct_date=date.split('-')
                for k in range(len(correct_date)):
                    try:
                        correct_date[k]=int(correct_date[k])

                    except:
                        continue
                dt=correct_date.join('/')
                row["Odometer_Reading"]=int(row["Odometer_Reading"])
                row["Trip_Distance"]=int(row(["Trip_Distance"]))
                cleaned_rows.append(row)
            except:
                continue
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    for row in cleaned_rows:
        cur.execute('Insert into trips(VehicleID,StartDate,EndDate,DriverName,StartDate,DistanceKm) values(?,?,?,?,?,?)',(row['VehicleID'],dt,dt,row['Driver'],row['Odometer_Reading'],row['Trip_Distance']))
    conn.commit()

@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)