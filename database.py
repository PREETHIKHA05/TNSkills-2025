import sqlite3
db_name='vehicle.db'
def create_tables():
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    cur.execute('''CREATE Table Vehicles(
                VehicleID TEXT PRIMARY KEY,
                RegNo TEXT,
                Type TEXT,
                LastServiceDate TEXT,
                CurrentOdometer INTEGER,
                LastServiceOdometer INTEGER)
                ''')
    conn.commit()
    cur.execute('''CREATE TABLE TRIP(
                TripID INTEGER PRIMARY KEY AUTOINCREMENT,
                VehicleID INTEGER,
                DriverName TEXT,
                StartDate TEXT,
                EndDate TEXT,
                DistanceKm INTEGER,
                FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    conn.commit()
    cur.execute('''CREATE TABLE MAINTANENCE_ALERTS(
                    ALERT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    VehicleID INTEGER,
                    ALERT_DATE DATETIME,
                    REASON TEXT,
                    FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    conn.commit()
    cur.execute('''CREATE TABLE Service_History(
                    Service_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    VehicleID INTEGER,
                    ServiceDate DATETIME,
                    OdometerReading INTEGER,
                    Notes TEXT,
                    FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    conn.commit()

def insert_values():
    conn=sqlite3.connect(db_name)
    

    