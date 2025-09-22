def calculator():
    num1=int(input("Enter the First number:"))
    num2=int(input("Enter the second number:"))
    print("What operation you want to perform")
    print("Addition = 1 \n subtraction = 2 \n division = 3 \n multiplication = 4")
    choice =int(input("enter choice (1,2,3,4) :"))

    if choice==1:
        c = num1+num2
        print(f"And the Addition is :{c}")
        pass