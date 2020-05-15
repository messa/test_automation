"""
file name: HW1.py
autor: medulka
created: 2020-05-14

Write a program in Python or Java that counts backwards from 100 to 1 
and prints: “Agile” if the number is divisible by 5, 
“Software” if the number is divisible by 3, 
“Testing” if the number is divisible by both, 
or prints just the number if none of those cases are true. 

"""

# A) Get one value for the number divisible by 15

def function_to_test_me():
    for x in range(100, 0, -1):
        if x%5 == 0 and x%3 != 0:
            print("Agile")
        elif x%3 == 0 and x%5 != 0:
            print("Software")
        elif x%3 == 0 and x%5 == 0:
            print("Testing")
        else: print(x)
    
function_to_test_me()  

# B) Get three values for the number divisible by 15
     
def function_to_test_me():
    for x in range(100, 0, -1):
        if x%5 == 0 and x%3 != 0:
            print("Agile")
        elif x%3 == 0 and x%5 != 0:
            print("Software")
        elif x%3 == 0 and x%5 == 0:
            print("Agile Software Testing")
        else: print(x)    

function_to_test_me()  
