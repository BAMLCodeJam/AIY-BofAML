##
## Ask your user for the answer of this question: "Who is my lover?" (or best friend or worst enemy)
## Only if he gets it right you will print "success"
##
## To read something from the console you can use:
## myVariable = input("Please enter something here: ")
## my varibale will contain the value of what has been entered in the console.
## The use needs to press "Enter"
##
## Think on how to use test if something is right or wrong.

def main():
    # your code here
    
    myLover = "Mum"
    while True:
        myVariable = input("Who is my lover? ")
        if myLover == myVariable:
            print("Well done")
            return
        else:
            print("No")

    return


if __name__== '__main__':
    main()