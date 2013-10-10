def getsum():
    a = 1
    b = 2
    summary = 2
    while b <= 4000000:
        a,b = b,a + b
        if b % 2 == 0:
            summary += b
    return summary
print getsum()
            
