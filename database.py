import sqlite3
db_name='vehicle.db'
def create_tables():
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    cur.execute('''CREATE Table Vehicles(
                VehicleID INTEGER PRIMARY KEY,
                RegNo TEXT,
                Type TEXT,
                LastServiceDate DATETIME,
                CurrentOdometer INTEGER,
                LastServiceOdometer INTEGER)
                ''')
    conn.commit()
    cur.execute('''CREATE TABLE TRIP(
                TripID AUTOINCREMENT PRIMARY KEY,
                VehicleID INTEGER,
                DriverName TEXT,
                StartDate DATETIME,
                EndDate DATETIME,
                DistanceKm INTEGER
                FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID)''')
    conn.commit()
    cur.execute('''CREATE TABLE MAINTANENCE_ALERTS(
                    ALERT_ID PRIMARY KEY AUTOINCREMENT,
                    VEHICLE_ID INTEGER,
                    ALERT_DATE DATETIME,
                    REASON TEXT,
                    FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    conn.commit()
    cur.execute('''CREATE TABLE Service_History(
                    Service_ID INTEGER PRIMARYKEY,
                    VehicleID INTEGER,
                    ServiceDate DATETIME,
                    OdometerReading INTEGER,
                    Notes TEXT,
                    FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID)))''')
    conn.commit()
    
    