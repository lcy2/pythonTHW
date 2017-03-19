def find(num):
    count2 = count5 = 0
    for i in xrange(1, num + 1):
        while i % 5 == 0:
            count5 += 1
            i /= 5
            
    return count5