x=int(input())
xx = x//2
count= 0
 
for i in range(1,x):
  if x%i==0 :
    print(i)
    print(x//i)
    
  if (x//i)<i:
      break
