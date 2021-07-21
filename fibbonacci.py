a=0
b=1
i=2
n=int(input("Enter a valid number: "))
if n<2:
    print(n)
else:
    print(a,b,end=" ")
    while i<n:
        sum=a+b
        print(sum,end=" ")
        a=b
        b=sum
        i=i+1


