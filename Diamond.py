
print("print diamond with star")
n=int(input("enter a number of row "))
# for upward pattern
sp=n*2 +8
for i in range(0,n):
	for j in range(0,sp):
		print(end=" ")
	sp=sp-1
	for j in range(0,i+1):
	 	print("*",end=" ")
	print(" ")
#for downward pattern 
sp=n*2
for i in range(n+1,0,-1):
	for j in range(sp,0,-1):
		print(end=" ")
	sp=sp+1
	for j in range(0,i):
		print("*",end=" ")
	print(" ")
	                                                          
