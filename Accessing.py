#Accessing Nested list using for loop 
a=[7,29,30,42,[5,6]]
l=len(a)
print("the lenght of nested list is = ",l)
print("index    value ")
for i in range(0,l):
    if type(a[i]) is list:
        for j in range(0,len(a[i])):
            print(i, j ,  "     "    ,  a[i][j])
    else:
        print(i,"       "     ,   a[i])
