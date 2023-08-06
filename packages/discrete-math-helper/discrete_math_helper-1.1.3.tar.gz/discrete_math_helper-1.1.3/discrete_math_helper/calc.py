import math
import sys

class Calculator:
    def combination(self, n, r):
        if(n < r):
            print("Invalid values for n and r.\n")
            exit(1)
        ans = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
        print("The answer for this combination is:", ans , "\n")

    def permutation(self, n, r):
        if(n < r):
            print("Invalid values for n and r.\n")
            exit(1)
        ans = (math.factorial(n))/math.factorial(n-r)
        print("The answer for this permutation is:", ans , "\n")

    
    def truthtable(self, argument):
        numDashes = 24 + 3 + 4 + len(argument) + 1
        for x in range(numDashes):
            print("-", end="")
        print("\n|     p     |     q     |   ", argument)
        for x in range(numDashes):
            print("-", end="")
        argument = argument.replace("xor", "!=")
        p = False
        q = False
        print("\n|   False   |   False   |   ", eval(argument))
        for x in range(numDashes):
            print("-", end="")
        p = True
        q = True
        print("\n|   True    |   True    |   ", eval(argument))
        for x in range(numDashes):
            print("-", end="")
        p = True
        q = False
        print("\n|   True    |   False   |   ", eval(argument))
        for x in range(numDashes):
            print("-", end="")
        p = False
        q = True
        print("\n|   False   |   True    |   ", eval(argument))
        for x in range(numDashes):
            print("-", end="")
        print("\n")

    def bayes(self, pta, pa, pt):
        ans = (pta*pa)/(pt)
        print("The answer for this bayes probabilty problem is:",ans,"\n")

    def bigo(self, a , b , d):
        if (a/(b ** d) < 1):
            print("O(n) = O(n **",d, ")\n")  
        elif (a/(b ** d) == 1):
            print("O(n) = O((n **",d,") * log(n))\n")
        elif (a/(b ** d) > 1):
            print("O(n) = O(n ** (log(",b,")(",a,")))\n")
