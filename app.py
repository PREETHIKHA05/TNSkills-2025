from flask import Flask, render_template
import csv
from database import create_tables
create_tables()
app=Flask(__name__)


def parse_vehicles_data(file):
    cleaned_rows=[]
    with open(file,'r') as f:
        readerObject=csv.DictReader(f)
        for row in readerObject:
            try:
                row["CurrentOdometer"]=int(row["CurrentOdometer"])
                row["LastServiceOdometer"]=int(row(["LastServiceOdometer"]))
                cleaned_rows.append(row)
            except:
                continue
@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)