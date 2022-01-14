print(" example of break ")
i=0
while i<10:
    print("number" + str(i))
    if i==5:
        break
    i=i+1
    

print("example of continue function")
for i in range(10):
    if i == 5:                  #if i%2!=0:
       continue
    print("yes", i)
    
print("example of pass function")
# pass is a null statment in python
#pass function instructs to do nothing 
for i in range(10):
    if i==5:    # this means if i==5 do nothing
        pass
    print("hello",i)
 
