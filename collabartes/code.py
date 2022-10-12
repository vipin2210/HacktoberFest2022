def comp(n):
    for i in range (4,n+1):
        for j in range(2,i):
            if i % j == 0 :
                print(i)
                break

t = int(input("Enter a number"))

while(t >=1 & t <= 50):
        for k in range(0,t):
            p = int(input(""))
            if(p >=4 & p <= 10000):
                comp(p)
