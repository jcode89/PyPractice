'''
A CLI program that finds all the prime factors of the number you enter.
Just type --> pypy sieveofatkins.py limit_number choice
choice is either yes or no depending on whether you want the list of primes saved.
i.e. pypy sieveofatkins.py 500000 yes
     "Enter name of file > 'Atkins.txt'"
'''
from math import sqrt
from sys import argv
#import numpy as np


def sieve_of_atkins(num):
    prime = [2, 3]
    #is_prime = np.array([False] * (num + 1))
    is_prime = [False] * (num + 1)

    for x in range(1, int(sqrt(num))+1):
        for y in range(1, int(sqrt(num))+1):
            n = 4*x**2 + y**2
            if n <= num and (n%12==1 or n%12==5):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if n <= num and n%12==7:
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if x > y and n <= num and n%12==11:
                is_prime[n] = not is_prime[n]
    for x in range(5, int(sqrt(num))):
        if is_prime[x]:
            for y in range(x**2, num+1, x**2):
                is_prime[y] = False
    for p in range(5, num):
        if is_prime[p]:
            prime.append(p)
    return prime

def find_factors(some_number ,some_list):
    results = []
    try:
        for number in some_list:
            if some_number % number == 0:
                results.append(number)        
        return results, "The largest prime factor is: %d" %  max(results)
    except ValueError:
        return "Woops looks like %d is a prime" % some_number

def atkins_to_file(listname, filename):
    with open(filename, 'w') as atpr:
        for item in listname:
            atpr.write(str(item) + '\n')

if __name__ == '__main__':
    #script, limit, filename = argv
    script, limit, choice = argv
    plimit = int(sqrt(int(limit)))
    if choice.lower() == 'yes':
        filename = input("Enter name of file > ")
        atkins_to_file(sieve_of_atkins(plimit), filename)
        print("File saved succesfully!")
    elif choice.lower() == 'no':
        # A number will never have a prime factor greater than the
        # square root of that number.
        primes = sieve_of_atkins(plimit)
        print(find_factors(int(limit), primes))
    else:
        print("Woops, start over!")
