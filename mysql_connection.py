import mysql.connector as myconn
h=input("Enter hostname : ")
u=input("Enter Username : ")
p=input("Enter password : ")
conn=myconn.connect(host=h,user=u,passwd=p)
if conn:
    print("Connection Successfull.......")
else:
    print("Connection Denied.......")
print()
input("Press ENTER to continue...........")
print()
curr=conn.cursor()
curr.execute("show databases")
print()
print("=====================Database in the MySql===========================")
print()
for a in curr:
    print(a)
print()
db=input("Select database : ")
curr.execute("use "+db)
print()
curr.execute("show tables")
print("====================Tables in Database=======================")
print()
for b in curr:
    print(b)
ch='y'
while(ch in 'yY'):
    q=input("Enter your querry to run : ")
    curr.execute(q)
    print("======================RESULT==================================")
    print()
    for c in curr:
        print(c)
    print()
    ch=input("If want to write more querry type 'y' or 'Y' : ")
    
