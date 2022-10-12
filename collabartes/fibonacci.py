terms=int(input("How many terms you want?"))
n1,n2=0,1
count=0
if terms<0:
    print("Enter positive number")
elif terms==1:
    printf("Fibonacci series upto",terms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<terms:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
