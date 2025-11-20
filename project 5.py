'''
Simple Calculator Program 
'''

def add(num1,num2):
    return num1+num2 

def sub(num1,num2):
    return num1-num2 

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2



def show_menu():
    print("\n---Calculator---")
    print("1.addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")


while True:
        show_menu()

        choice = input("Enter your choice : ")
        
        if (choice == "1"):
            num1 = float(input("Enter the first number  : "))
            num2 = float(input("Enter the second number : "))
            print(f"The Addition is {add(num1,num2)}")

        elif(choice == "2"):
            print(f"The Subtraction is {sub(num1 , num2 )}")


        elif(choice == "3"):
            print(f"The Multiplication is {mul(num1,num2) }")


        elif(choice == "4"):
            if (num2 == 0):
                print("Division cannot performed!")

            else:
                print(f"The Division is {div(num1 , num2)}")

        elif(choice == "5"):
            print("Exiting program!")

        else:
            print("invalid choice!")




