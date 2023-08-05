import math
import sys

if(len(sys.argv) < 2):
    print("The argument list is too short")
    exit(1)

problemtype = sys.argv[1]

if problemtype == "combination":
    if(len(sys.argv) < 4):
        print("The argument list is too short")
        exit(1)
    n = int(sys.argv[2])
    r = int(sys.argv[3])
    if(n < r):
        print("Invalid values for n and r.\n")
        exit(1)

    ans = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
    print("The answer for this combination is:", ans , "\n")

if problemtype == "permutation":
    if(len(sys.argv) < 4):
        print("The argument list is too short")
        exit(1)
    n = int(sys.argv[2])
    r = int(sys.argv[3])
    if(n < r):
        print("Invalid values for n and r.\n")
        exit(1)

    ans = (math.factorial(n))/math.factorial(n-r)
    print("The answer for this permutation is:", ans , "\n")

if problemtype == "truth-table":
    if(len(sys.argv) < 3):
        print("The argument list is too short")
        exit(1)
    argument = sys.argv[2]

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

if problemtype == "bayes-prob":
    if(len(sys.argv) < 5):
        print("The argument list is too short")
        exit(1)
    pta = int(sys.argv[2])
    pa = int(sys.argv[3])
    pt = int(sys.argv[4])
    ans = (pta*pa)/(pt)
    print("The answer for this bayes probabilty problem is:",ans,"\n")

if problemtype == "big-o":
    if(len(sys.argv) < 5):
        print("The argument list is too short")
        exit(1)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    d = int(sys.argv[4])

    if (a/(b ** d) < 1):
        print("O(n) = O(n **",d, ")\n")  
    elif (a/(b ** d) == 1):
        print("O(n) = O((n **",d,") * log(n))\n")
    elif (a/(b ** d) > 1):
        print("O(n) = O(n ** (log(",b,")(",a,")))\n")
