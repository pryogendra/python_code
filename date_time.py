import datetime as dt
name=input("Enter your name :")
age=int(input("Enter your age :"))
year_now=dt.datetime.now()
print(year_now.year)
print("You will turn 100 in "+str(int(100-age)+int(year_now.year)))
