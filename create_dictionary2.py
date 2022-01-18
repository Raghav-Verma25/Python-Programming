
d={}
print("How manty element to be inserted")
n=int(input())
for i in range(0,n):
    print("Enter key= ")
    k=input()
    print("enter value= ")
    v=int(input())
    d.update({k:v})
print(d)
