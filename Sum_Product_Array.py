
a=[1,2,3,5,10]
sum=0
pro=1
l=len(a)
print(l)
i=0
while l>0:
	pro=pro*a[i]
	sum=sum+a[i]
	i=i+1
	l=l-1
print(pro)
print(sum)
