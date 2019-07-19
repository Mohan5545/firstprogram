m,n=map(int,input().split())
for i in range(m+1,n):
    for j in range(2,i):
         if(i%j==0):
           break
    else:
        print(i,end=" ")
