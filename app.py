from flask import Flask, render_template, request
import csv
from database import create_tables
import sqlite3
db_name='vehicle.db'
create_tables()
app=Flask(__name__)
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_availability',methods=['GET','POST'])
def check_availability():
     if request.method=='POST':
          start_date=request.form.get('start_date')
          end_date=request.form.get('end_date')
          conn=sqlite3.connect(db_name)
          cur=conn.cursor()
          cur.execute('Select vehicleID,StartDate,EndDate from trip')
          available=cur.fetchall()
          vehicles_avail=[]
          for id,s,e in available:
               if e>end_date and s<start_date:
                    vehicles_avail.append(id)
          return render_template('check_availability.html',vehicles_avail=vehicles_avail)
     if request.method=='GET':
          return render_template('check_availability.html')
if __name__=='__main__':
    app.run(debug=True)