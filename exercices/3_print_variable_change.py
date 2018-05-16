##
## Define a variable and print the content of the variable in the console.
## Change the value of the variable and print it again.
##


def main():
    MYmessage = "hello stawberry"
    print(MYmessage)
    
    mymessage = "hello strawberries"
    print(mymessage)
    
    mymessage= MYmessage + " toto " + mymessage
    print(mymessage)
    
    return

if __name__== '__main__':
    main()