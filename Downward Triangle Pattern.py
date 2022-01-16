"""              * * * * * * * * * * * 
                   * * * * * * * * * * 
                    * * * * * * * * * 
                     * * * * * * * * 
                      * * * * * * * 
                       * * * * * * 
                        * * * * * 
                         * * * * 
                          * * * 
                           * * 
                            *"""
                            
print("Downward Triangle Pattern")
n= int(input("enter a number of row"))
sp=n*2
for i in range(n+1,0,-1):
	for j in range(sp,0,-1):
		print(end=' ')
	sp=sp+1
	for j in range(0,i):
		print("*",end=' ')
	print(" ")
