"""Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']"""

qq=['p','q']
print(qq)
n=int(input())
list=[]
for i in range(1,n+1):
    list.append(i)
print("the second list is ",list)
#for i in range(0,n):
l4=['{}{}'.format(i,j) for i in qq for j in list] 
print("concatenation ",str(l4))
    
