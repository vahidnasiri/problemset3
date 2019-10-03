import sys

if len(sys.argv) != 3:
    print("Usage: python " + sys.argv[0] + " <first word> <second word>")
    sys.exit()

firstword = sys.argv[1]
secondword = sys.argv[2]

def spellBackwards(firstword):
    resultback=""
    resultback=firstword[::-1]
    return resultback

def capitalize (secondword):
    resultcap=""
    for i in range (0,len(secondword)):
        a=secondword[i].capitalize()
        resultcap=resultcap+a
    return resultcap
    
backwards = spellBackwards(firstword)
capital = capitalize(secondword)

def threadTogether(firstword, secondword):
    result=""
    b=min(len(firstword), len(secondword)) 
    for i in range (0,b):
        a = firstword[i]+ secondword[i]
        result = result + a
    if len(firstword)>b:
        for i in range(b, len(firstword)):
            result= result+ firstword[i]
    if len(secondword)>b:
        for i in range (b, len(secondword)):
            result = result+ secondword[i]     
    return (result)
    
threaded = threadTogether(backwards, capital)

def printitOut(firstword,secondword):
    #return spellBackwards(firstword), capitalize(secondword), threadTogether(backwards,capital)
    print ("The reverse of"+" "+ firstword +" "+"is"+" "+ backwards+ ".")
    print("The capital of"+" "+ secondword +" "+"is"+" "+ capital + ".")
    print ("Thread, they become"+" "+ threaded+".")
    
printitOut(firstword, secondword)