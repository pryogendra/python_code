try:
    f=open("null.txt")
    f_read=f.read()
    print(f_read)
    f.close()
except Exception as e:
    print("Error is generated .....")
    print("Error type : ",e)
