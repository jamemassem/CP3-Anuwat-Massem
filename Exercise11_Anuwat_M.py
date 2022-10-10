'''
5
----* 0
---*** 1        
--***** 2
-******* 3
********* 4
'-' => ' '
''' 
n = int(input()) 

for i in range(n): # 0 1 2 3 4 
    for j in range(n+i): # 5 6 7 8 9 
      if  j < (n-1)-i:
        print(' ',end='')   
      else:
        print('*',end='')
    print()