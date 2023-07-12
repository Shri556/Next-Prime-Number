#Have the program find prime numbers until the user chooses to stop asking for the next one.
from time import sleep

def prime_checker(n):
    if n % 2 ==0:
        print("Not a Prime Number!! That's a EVEN Number")
        return False
    if n == 2:
        print("2 is a Prime Number!!")
        return False
    
    for i in range(3,int((n**0.5)+1),2):
        if n % i == 0:
            return False
    else:
        print("That's a Prime Number!!")
        return True
    


def next_prime_gen(x):
    new_prime = x + 1

    while True:
        if not prime_checker(new_prime):
            new_prime += 1
        else:
            break
    print(new_prime)

def cover():
    
    trash = []

    while True:
        Firstinput = input("Please Enter a Numeric Value: ")

        if Firstinput.isnumeric():
            int_input = int(Firstinput)
            break
        else:
            print("Please Enter a Valid Input")
    
    prime_checker(int_input)
    while True:
        Cont = input("Do you want to get next Five prime Number('Y' or 'N'): ")

        if Cont.lower() == 'y':
            
            next_prime_gen(int_input)
                
        
        if Cont.lower() == 'n':
            print("Exiting")
            sleep(5)
            print("BYE")
            break
        
        if Cont.lower() not in ['y','n']:
            print("That's not a Valid input ")
            sleep(5)

        



cover()