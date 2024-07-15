name=(input("Enter name:"))
rollno=(int(input("Enter rollno:")))
print("Subject marks out of 100")
a=(int(input("English:")))
b=(int(input("Maths:")))
c=(int(input("Science:")))
d=(int(input("Gujrati:")))
e=(int(input("Hindi:")))
if(a>30 and b>30 and c>30 and d>30 and e>30):
    total=a+b+c+d+e
    print("Total marks out of 500:",total)
    avg=total/5
    print("Average is:",avg)
    if(avg>=90):
        print("Grade A")
    elif(avg<=89 and avg>=80):
        print("Grade B")
    elif(avg<=79 and avg>=50):
        print("Grade C")
    elif(avg<=49 and avg>=30):
        print("Grade D")
    else:
        print("You are Fail")
else:
    print("You are Fail better luck next time")