import sqlite3
db_name='vehicle.db'
def create_tables():
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    cur.execute('''CREATE Table  Vehicles(
                VehicleID INTEGER PRIMARY KEY,
                RegNo TEXT,
                Type TEXT,
                LastServiceDate DATETIME,
                CurrentOdometer INTEGER,
                LastServiceOdometer INTEGER)
                ''')