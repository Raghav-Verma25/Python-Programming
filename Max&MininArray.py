a=[4 ,2,5,20,6,7]
i=0
large=a[0]
l=len(a)
while l>0:
	if a[i]>large:
		large=a[i]
	i=i+1
	l=l-1
print("largest is ")
print(large)
i=0
l=len(a)
print("smaller is")
smaller=a[0]
while l>0:
	if a[i]<smaller:
		smaller=a[i]
	i=i+1
	l=l-1
print(smaller)
