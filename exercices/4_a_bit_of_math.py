
## Calculate the value of 1 billion divided by 53000 multiple by the sum of first 100 numbers (1 to 100)
## You need to use variables
## You can use the a for loop and range
## For example try:
## for i in range(0,5):
##    print (i)
##
## Think about how to save the sum in each loop or your for loop

def main():
    message="calculate what I tell you to. The result is: "
    calculatrice = 1000000000 / 53000
    print (message + str(calculatrice))
    print(calculatrice + 2)
    calculator = 0
    for i in range(0,100000001):
        print(i)
        print("+")
        calculator = calculator + i
                          
        
    message="calculate what i tell you to. The result is: "
    print (message + str(calculatrice))  
    print(calculator)
    message="the result is:"
    print(message) 
    result=calculatrice*calculator
    print (result)
    
    print("-------")
    print(calculatrice)
    print(i)
    print(calculator)
    print(message)
    print(result)
                            
    return

if __name__== '__main__':
    main()