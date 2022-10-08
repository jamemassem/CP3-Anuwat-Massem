#The program will allow the user (teacher) to enter his or her student's score.
FE = int(input('Please input Foundation English score : ')) 
GB = int(input('Please input General Business score : '))  
ITCS = int(input('Please input Introduction to Computer Systems score : ')) 
CP = int(input('Please input Computer Programming score : ')) 

#Output
print(f'''-------------------- Your Score --------------------
Foundation English                : {FE}   points
General Business                  : {GB}   points  
Introduction to Computer Systems  : {ITCS}   points
Computer Programming              : {CP}   points
----------------------------------------------------''')