
print("to check wether a triangler is isosceles or scalene or right angle triangle or invalid")
a=int(input("enter one side="))
b=int(input("enter 2 side="))
c=int(input("enter 3 side="))
#if a+b+c==180:
#	print("triangle is valid and")
if a==b==c:
		print("equilateral")
elif a==b or b==c or c==a:
		print("iso")
elif ((a**2)+(b**2))==(c**2) or ((b**2)+(c**2))==(a**2) or ((c**2)+(a**2))==(b**2):
		print("right angle triangle")
else:
		print("scalene")

"""else:
	print("triangle not valid")"""
