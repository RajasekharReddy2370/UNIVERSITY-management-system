import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database = 'ums',
    user = 'root',
    password = 'Raj@2370'
)

cur = conn.cursor()

class update():
    def departmentupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update department set {columnname}='{newvalue}' where {columnname} = '{oldvalue}' ")
        conn.commit()
        print(" Data has been inserted successfully")

    
    def courseupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update course set {columnname}='{newvalue}' where {columnname} = '{oldvalue}' ")
        conn.commit()
        print(" Data has been inserted successfully")


    def facultyupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update faculty set {columnname} = '{newvalue}' where {columnname} = '{oldvalue}' ")
        conn.commit()
        print(" Data has been inserted successfully")


    def studentupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update course set {columnname} = '{newvalue}' where {columnname} = '{oldvalue}' ")
        conn.commit()
        print(" Data has been inserted successfully")


