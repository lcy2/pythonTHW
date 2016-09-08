


def whileLoop(number, inc):
    i = 0
    numbers = []
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    print "The numbers: "
    

    
whileLoop(7,2)


def forLoop(number, inc):
    numbers = []
    for i in range(0, number, inc):
        print "At the top i is %d" % i
        
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers
print "The numbers: "
numbers = forLoop(7,2)
for num in numbers:
    print num