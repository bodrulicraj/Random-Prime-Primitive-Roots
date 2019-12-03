import random
from math import gcd
def checkPrime(number): 
    counter = 0
    if (number <= 1): 
        return False
    if (number <= 2): 
        return True
    for i in range(2, number):
        if (number % i) == 0:
            counter = counter + 1
    if counter == 0:
        return True
    else:
        counter = 0
        return False
		
def primitiveRoots(primeNum):
    possible_set = {num for num in range(1, primeNum) if gcd(num, primeNum) }
    root_list = [base for base in range(1, primeNum) if possible_set == {pow(base, power, primeNum) for power in range(1, primeNum)}]
    return root_list
	
if __name__ == '__main__':
    print("Set Lower Limit: ")
    lowerLimit = int(input())
    print("Set Upper Limit: ")
    upperLimit = int(input())
    primes = [i for i in range(lowerLimit,upperLimit) if checkPrime(i)]
    randomPrime = random.choice(primes)
    error = str(randomPrime) + ' is not a Prime Number!'
    if (checkPrime(randomPrime)):
        print('Primitive Roots of ' + str(randomPrime) + " are: ")
        roots = primitiveRoots(randomPrime)
        print(roots)
        print("Number of Roots: " + str(len(roots)))
    else :
        print(error)