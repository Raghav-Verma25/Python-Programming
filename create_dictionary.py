

d={}
tup=()
print("How manty element to be inserted")
n=int(input())
for i in range(0,n):
    print("Enter key= ")
    k=input()
    print("enter value= ")
    v=eval(input())
    d.update({k:v})
print(d)



