import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    database = 'ums',
    user = 'root',
    password = 'Raj@2370'
)

cur = conn.cursor()


class insert:

    def departmentinsert(x,departmentid,departmentname):
        cur.execute(f"insert into department values ({departmentid},'{departmentname}')")
        conn.commit()
        print(" Data has been inserted successfully")

    def courseinsert(x,courseid,coursename,coursefee,duration):
        cur.execute(f"insert into course values ({courseid},'{coursename}',{coursefee},{duration})")
        conn.commit()
        print("Data entered successfully")
    
    def facultyinsert(x,facultyid,facultyname,departmentid,salary,courseid):
        cur.execute(f"insert into faculty values({facultyid},'{facultyname}',{departmentid},{salary},{courseid})")
        conn.commit()
        print("Data inserted successfully")

    def studentinsert(x,sid,sname,courseid,departmentid):
        cur.execute(f"insert into student values ({sid},'{sname}',{courseid},{departmentid})")
        conn.commit()
        print("Data entered successfully")
        


   
















