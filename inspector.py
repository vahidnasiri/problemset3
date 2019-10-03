import sys

if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " <number>")
    sys.exit()

number = int(sys.argv[1])

#print("{0}".format(number))

def isOdd(number):
    if number%2!= 0:
        result = "The number"+ " "+str(number) +" " + "is odd."
    if number%2==0:
        result = "The number"+ " "+str(number) +" " + "is not odd."
    return result

def isSquare(number):
    x = number // 2
    y = set([x])
    while x * x != number:
        x = (x + (number // x)) // 2
        if x in y:
            return "The number"+" "+ str(number)+" "+"is not square."
        y.add(x)
    return "The number"+" "+str(number)+ " "+ "is square."

def isIncreasing(number):
    digit= [int(x) for x in str(number)]
    i=0
    while i<len(digit):
        if i+1== len(digit):
            return ("The number"+" "+str(number)+" "+"is increasing.")
        elif digit[i]<=digit[i+1]:
            i=i+1
        else:
            return ("The number"+" "+str(number)+" "+"is not increasing.")

def isPalindorme(number):
    if str(number)==str(number)[::-1]:
        return ("The number"+" "+str(number)+" "+"is a palindorme.")
    else:
        return ("The number"+" "+str(number)+" "+"is not a palindorme.")
    
    
def isFactorial(number):
    result=str(number)
    i=1
    if number==1:
        print ("The number"+" "+ str(number) +" "+"is a factorial.")
    elif number==0:
        print("The number"+" "+ str(number) +" "+"is not a factorial.")
    else:
        while number>1:
            if number % i == 0:
                number = number / i
                if number==1:
                    return ("The number"+" "+ result +" "+"is a factorial.")
            else:
                return ("The number"+" "+ result +" "+"is not a factorial.")
                break  
            i=i+1


def finalresults(number):
    #return isOdd(number), isSquare(number), isIncreasing(number), isPalindorme(number), isFactorial(number)
    print(isOdd(number))
    print(isSquare(number))
    print(isIncreasing(number))
    print(isPalindorme(number))
    print(isFactorial(number))
    
finalresults(number)