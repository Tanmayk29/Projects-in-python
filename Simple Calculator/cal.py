def calculator():
    num1=int(input("Enter the First number:"))
    num2=int(input("Enter the second number:"))
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    choice =int(input("enter choice (1,2,3,4):"))

    if choice==1:
        result = num1+num2
    elif choice==2:
        result = num1-num2
    elif choice==3:
        result = num1*num2
    elif choice==4:
        if num2!=0:
            result=num1/num2
        else:
            print("ERROR!!!!,Pls enter proper number")
            return
    else:
        print("OPERATION is Invalid!!")
        return
    print(f"THE Answer is :{result}")
    

calculator()