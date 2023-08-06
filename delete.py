import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database = 'ums',
    user = 'root',
    password = 'Raj@2370'
)

cur = conn.cursor()

class delete:

    def departmentdelete(x,columnname,oldvalue):
        cur.execute(f"delete from department where {columnname} = '{oldvalue}' ")
        conn.commit()
        print("Data entered successfully")

    def coursedelete(x,columnname,oldvalue):
        cur.execute(f"delete from course where {columnname} = '{oldvalue}' ")
        conn.commit()
        print("Data entered successfully")

    def facultydelete(x,columnname,oldvalue):
        cur.execute(f"delete from faculty where {columnname} = '{oldvalue}' ")
        conn.commit()
        print("Data entered successfully")

    def studentdelete(x,columnname,oldvalue):
        cur.execute(f"delete from department where {columnname} = '{oldvalue}' ")
        conn.commit()
        print("Data entered successfully done")