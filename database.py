import sqlite3
db_name='vehicle.db'
def create_tables():
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    try:
        cur.execute('''CREATE Table Vehicles(
                    VehicleID TEXT PRIMARY KEY,
                    RegNo TEXT,
                    Type TEXT,
                    LastServiceDate TEXT,
                    CurrentOdometer INTEGER,
                    LastServiceOdometer INTEGER)
                    ''')
        cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V1", "REG-001" , "Truck" , "2025-05-20" , 20000 , 10000 ))
        cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_001" , "REG-101" , "Van" , "2025-10-01" , 50400 , 40400))
        cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_002" , "REG-102" , "Car" , "2025-11-15" , 12050 , 10000 ))
        cur.execute('insert into vehicles values( ?, ? , ?, ? ,?,?)',( "V_003" , "REG-103" , "Van" , "2025-08-20" , 8200 , 2000 ))
        conn.commit()
    except:
        pass
    conn.commit()
    try:
        cur.execute('''CREATE TABLE TRIP(
                    TripID INTEGER PRIMARY KEY AUTOINCREMENT,
                    VehicleID INTEGER,
                    DriverName TEXT,
                    StartDate TEXT,
                    EndDate TEXT,
                    DistanceKm INTEGER,
                    FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
        cur.execute('insert into trip values( ?, ? , ?, ? ,?,?)',( 1 , "V1" , "TestDriver" , "2025-12-20" , "2025-12-30 ",500))
        conn.commit()

    except:
        pass
    conn.commit()
    try:
        cur.execute('''CREATE TABLE MAINTANENCE_ALERTS(
                        ALERT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        VehicleID INTEGER,
                        ALERT_DATE DATETIME,
                        REASON TEXT,
                        FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    except:
        pass
    conn.commit()
    try:
        cur.execute('''CREATE TABLE Service_History(
                        Service_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        VehicleID INTEGER,
                        ServiceDate DATETIME,
                        OdometerReading INTEGER,
                        Notes TEXT,
                        FOREIGN KEY(VehicleID) REFERENCES Vehicles(VehicleID))''')
    except:
        pass
    conn.commit()

    
    

    