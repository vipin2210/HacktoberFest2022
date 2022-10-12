print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        n1= float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    if choice == '1':
            print(add(n1, n2))
    elif choice == '2':
            print(subtract(n1, n2))
    elif choice == '3':
            print(multiply(n1, n2))
    elif choice == '4':
            print(divide(n1, n2))
    else:
        print("Invalid Input")

