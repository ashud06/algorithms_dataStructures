def appendAtBegginningFront(x,L):
    return [x + element for element in L]

def bitStrings(n):
    #print('entered')
    #print(n)
    if n==0: return []
    if n==1: return ['0','1']
    else:
        #print('debug print')

        #print(appendAtBegginningFront("0",bitStrings(n-1)))
        #print(appendAtBegginningFront("1",bitStrings(n-1)))
        #print(appendAtBegginningFront("0",bitStrings(n-1))+appendAtBegginningFront("1",bitStrings(n-1)))
        return (appendAtBegginningFront("0",bitStrings(n-1))+appendAtBegginningFront("1",bitStrings(n-1)))

def alternateFunc(n):
    if n==0: return []
    if n==1: return [0,1]
    return [str(digit)+str(bits) for digit in alternateFunc(1) for bits in alternateFunc(n-1)]


print(alternateFunc(4))
print(bitStrings(4))