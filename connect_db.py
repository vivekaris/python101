import mysql.connector as dbcon
con=dbcon.connect(
    host='localhost',
    user='root',
    password='',
    database='company'
)
#print (con)

mycursor=con.cursor()
Q="select roll_num from students"
mycursor.execute(Q)
result=mycursor.fetchall()
print (result)


for x in result:
    print (x)

Q="insert into students(roll_num,name,class)values(%s,%s,%s)"
r=input("enter roll_num")
n=input("enter name")
w=input("enter class")


val=(int (r),n,int(w))
mycursor.execute(Q,val)
con.commit();
print(mycursor.rowcount,"row inserted")
