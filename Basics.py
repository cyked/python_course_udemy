n = int(input("Enter a number: "))
ar=[]
for n in range(1,n+1):
    ar.append(n)
print(*ar, sep='')