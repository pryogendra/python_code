with open("Sample.txt","w") as file:
    print("Enter the 5 lines sentences in the file :")
    for i in range(5):
        file.write(input())
with open("sample.txt") as file:
    read=file.readlines()
    for j in read:
        print(j)
