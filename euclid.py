"""
A recreation of Euclid's Algorithm for finding the GCD or Greatest Common Divisor.
"""
# Please take note after further research, this is the subtraction version.
# There is a more common division version, which, makes use of a while loop.
# https://en.wikipedia.org/wiki/Euclidean_algorithm
# The site above has several pseudo code examples for the different versions.
# They use a while loop in the division and subtraction versions.
# My example is done without the use of a while loop.
# I did not know much about Euclid, when I wrote this function.
# All I used was the flow chart from this source https://en.wikipedia.org/wiki/Algorithm

def find_gcd(a,b):
    if b == 0:
        #print(a)
        return a
    elif a > b:
        a = a - b
        print("a is %d" % a)
        return find_gcd(a,b)
    else:
        b = b - a
        print("b is %d" % b)
        return find_gcd(a, b)

if __name__ == '__main__':
    #assert(find_gcd(8, 12) == 4)
    print(find_gcd(8, 12))

    #assert(find_gcd(54, 24) == 6)
    print(find_gcd(54, 24))

    #assert(find_gcd(1071, 462) == 21)
    print(find_gcd(1071, 462))
