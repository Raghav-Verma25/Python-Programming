

list1 =  [10, 20, 23, 11, 17]
list 2 = [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
"""
print(" list 1")
list1=[]
a=int(input("enter number of element"))
for i in range(0,a):
	lst1=int(input())
	list1.append(lst1)
print(list1)

print("\n")
print("list 2")
list2=[]
b=int(input("enter number of element"))
for i in range(0,b):
	lst2=int(input())
	list2.append(lst2)
print(list2)

print("\n\n")

list3=[]

for num in list1:
	if(num % 2 != 0):
		list3.append(num)

for num in list2:
	if(num % 2 == 0):
		list3.append(num)
			
print(list3)		

		
		
