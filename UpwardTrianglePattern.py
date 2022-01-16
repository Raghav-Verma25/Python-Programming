"""        * 
             ** 
            ***
           ****
          *****
         ******* """
         
print("Downward Triangle Pattern")
n= int(input("enter a number of row"))
sp=n*2
for i in range(0,n):
	for j in range(0,sp):
		print(end=' ')
	sp=sp-1
	for j in range(0,i+1):
		print("*",end=' ')
	print(" ")


