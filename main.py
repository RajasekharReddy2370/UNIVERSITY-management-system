from insert import insert
from update import update
from delete import delete
from read import read

obj = insert()
obj1 = update()
obj2 = delete()
obj3 = read()

print("THIS IS UMS PROJECT")

print('** You can do 4 operation in ums database **')

print(' For ADDING the data write *add* ')
print(' For UPDATING the data write *update* ')
print(' For DELETING the data write *delete* ')
print(' For READING the data write *read* ')

opr = input('Enter any operation ')

if opr=='add':

    print('For inserting data in department table please press -1 : ')
    print('For inserting data in course table please press -2 : ')
    print('For inserting data in faculty table please press -3 : ')
    print('For inserting data in student table please press -4 : ')


    tab = int(input("please enter the number to insert data in the table : "))

    if tab==1:
        departmentid = int(input("Please enter departmentid:"))
        departmentname = input("Please enter departmentname:")
        obj.departmentinsert(departmentid,departmentname)

    if tab==2:
        courseid  = int(input("Please enter courseid : "))
        coursename  = input("Please the course name : ")
        coursefee  = int(input("Please enter the coursefee : "))
        duration  = int(input("Please enter the duration : "))
        obj.courseinsert(courseid,coursename,coursefee,duration)

    if tab==3:
        facultyid = int(input(" Please enter the facultyid : "))
        facultyname  = input("Please enter facultyname : ")
        departmentid  = int(input("Please enter the departmentid : "))
        sallary  = int(input("Please enter salary : "))
        courseid  = int(input("Please enter courseid : "))
        obj.facultyinsert(facultyid,facultyname,departmentid,sallary,courseid)

    if tab==4:
        sid = int(input("Please enter the sid : "))
        sname = str(input("Please enter sname : "))
        courseid  = int(input("Please enter courseid : "))
        departmentid = int(input("Please enter departmentid : "))
        obj.studentinsert(sid,sname,courseid,departmentid)

if opr == "update":

    print('For updating data in department table please press -1 : ')
    print('For updating data in course table please press -2 : ')
    print('For updating data in faculty table please press -3 : ')
    print('For updating data in student table please press -4 : ')


    tab = int(input("please enter the number to update data in the table : "))

    if tab==1:
        columnname = input("Please enter columnname : ")
        newvalue = str(input("Please enter newvalue : "))
        oldvalue = str(input("Please enter oldvalue : "))
        obj1.departmentupdate(columnname,newvalue,oldvalue)

    if tab==2:
        columnname = input("Please enter columnname : ")
        newvalue = str(input("Please enter newvalue : "))
        oldvalue = str(input("Please enter oldvalue : "))
        obj1.courseupdate(columnname,newvalue,oldvalue)

    if tab==3:
        columnname = input("Please enter columnname : ")
        newvalue = str(input("Please enter newvalue : "))
        oldvalue = str(input("Please enter oldvalue : "))
        obj1.facultyupdate(columnname,newvalue,oldvalue)

    if tab==4:
        columnname = input("Please enter columnname : ")
        newvalue = str(input("Please enter newvalue : "))
        oldvalue = str(input("Please enter oldvalue : "))
        obj1.studentupdate(columnname,newvalue,oldvalue)


if opr == "delete":

    print('For delete data in department table please press -1 : ')
    print('For delete data in course table please press -2 : ')
    print('For delete data in faculty table please press -3 : ')
    print('For delete data in student table please press -4 : ')


    tab = int(input("please enter the number to delete data in the table : "))

    if tab==1:
        columnname = input("Please enter columnname : ")
        oldvalue = str(input("Please enter oldvalue : "))
        obj2.departmentdelete(columnname,oldvalue)

    if tab==2:
        columnname = input("Please enter columnname : ")
        oldvalue = str(input("Please enter oldvalue : "))
        obj2.coursedelete(columnname,oldvalue)
        
    if tab==3:
        columnname = input("Please enter columnname : ")
        oldvalue = str(input("Please enter oldvalue : "))
        obj2.facultydelete(columnname,oldvalue)

    if tab==4:
        columnname = input("Please enter columnname : ")
        oldvalue = str(input("Please enter oldvalue : "))
        obj2.studentdelete(columnname,oldvalue)

if opr == "read":

    print('For read data in department table please press -1 : ')
    print('For read data in course table please press -2 : ')
    print('For read data in faculty table please press -3 : ')
    print('For read data in student table please press -4 : ')


    tab = int(input("please enter the number to read data in the table : "))

    if tab==1:
        obj3.departmentread()

    if tab==2:
        obj3.courseread()

    if tab==3:
        obj3.facultyread()

    if tab==4:
        obj3.studentread()