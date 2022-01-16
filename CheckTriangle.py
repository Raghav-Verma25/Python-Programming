
print("to check wether a triangler is isosceles or scalene or right angle triangle or invalid")
a=int(input("enter one side="))
b=int(input("enter 2 side="))
c=int(input("enter 3 side="))
if a+b+c==180:
	print("triangle is valid and")
	if a==b==c:
		print("equilateral")
	elif a==b or b==c or c==a:
		print("iso")
	else:
		print("scalene")

else:
	print("triangle not valid")
