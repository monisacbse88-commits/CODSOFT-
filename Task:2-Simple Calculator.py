#Simple Calculator
print("Simple Calculator")
print("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder")
while True:
    num1=int(input("Enter number:"))
    num2=int(input("Enter number:"))
    choice=int(input("Enter choice:"))
    if choice==1:
        res=num1+num2
    elif choice==2:
        if num2>num1:
            num1,num2=num2,num1
        res=num1-num2
    elif choice==3:
        res=num1*num2
    elif choice==4:
        if num2==0:
            print("Zero Division error has occured")
            continue
        res=num1/num2
    elif choice==5:
        if num2==0:
            print("Zero division error occured")
            continue
        res=num1%num2
    print("Result:",res)
    c=input("Do you want to continue(y/n):")
    if(c=='n'):
        break
print("All arithmetic operations are performed successfully!!")
