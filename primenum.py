n = 29
l=n//2

l=l+2
flag=0
print(l)
for i in range(2,l):
    if(n%i!=0):
        flag=1
       
    else:
        flag=0
        break;
if flag==1:
    print("prime")        
else:
    print("not prime")    