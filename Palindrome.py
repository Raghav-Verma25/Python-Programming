

print("enter a number if reverse of given number = original number then print TRUE else FALSE \n OKK then let GOO ")
n=int(input())
print("u enter",n)     
on=n                                  #n= number    rn= reverse number   r=reminder   on=original number
rn=0
while n>0:
	r=n%10
	rn=(rn*10)+r
	n=n//10

if rn==on:
	print("TRUE")
else:
	print("FALSE")
