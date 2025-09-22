def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("error zerodivion")
    return a/b

while True:
    print("------calculator-------")
    print("1.Addiction")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")


    choice=input("enter the choice between(1-5):")
    if choice=='5':
        print("Exiting..........")
        break
    
    if choice in ['1','2','3','4']:
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number:"))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", sub(num1, num2))
        elif choice == '3':
            print("Result:", mul(num1, num2))
        elif choice == '4':
            print("Result:", div(num1, num2))
    else:
        print("Invalid input")
