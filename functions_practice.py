def add(a,b):
    return a+b
    
def subtract(a,b):
    return a-b
   
def multiply(a,b):
    return a*b
    
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b

while True:
    print("\n====CALCULATOR===")
    print("1.Add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.Exiting")

    try:
        choice=int(input("Chose an option: "))
    except ValueError:
        print("Nubers only")
        continue

    if choice==5:
        print("Existing....")
        break

    if choice not in [1,2,3,4]:
        print("Invalid options, choose 1-5")
        continue

    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    except ValueError:
        print("Please enter numbers only")

    if choice==1:
        print(f"Result: {add(num1,num2)}")

    if choice==2:
        print(f"Result: {subtract(num1,num2)}")

    if choice==3:
            print(f"Result: {multiply(num1,num2)}")

    if choice==4:
            print(f"Result: {divide(num1,num2)}")

