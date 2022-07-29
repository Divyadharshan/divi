u=int(input("Enter limit ="))

for j in range(2,u+1):
     for i in range(2,j):
          if j%i==0:
               break
     else:
          print(j)
            
