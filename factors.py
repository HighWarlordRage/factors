#Title: Project-3b
integer =  int(input("Please enter a positive integer: "))
print("The factors of",integer,"are:")
for dasa in range(1,integer+1):
    if(integer%dasa==0):
        print(dasa)


