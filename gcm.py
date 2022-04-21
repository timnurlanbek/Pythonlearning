n1 = int(input("enter a num: "))
n2 = int(input("enter a sec num"))
def gcm(n1,n2):
    if n1>0 and n2>0:
        if n1== n2:
            return n1
        elif n1>n2:
            min = n2
            max = n1
        else:
            min = n1
            max = n2
    if max% min == 0:
        return min
    else: 
        for k in range(min,0,-1):
            if (n1% k == 0) and (n2 % k == 0):
                return k

print(gcm(n1,n2))