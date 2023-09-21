dict1={1:10,4:40,7:70,5:50,6:60,2:20,3:30}
a=list(dict1.keys())
a.sort()
b=a
print("Ascending Order: ")
for i in a:
    print(str(i)+":"+str(dict1[i]))
print("Descending Order :")
b.reverse()
for i in b:
    print(str(i)+":"+str(dict1[i]))
