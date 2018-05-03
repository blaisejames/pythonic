def coinTosses():
    import random
    heads, tails, result = 0, 0, 0
    print "Starting the program..."
    for i in range(1, 5001):
        print "Attempt #{}: Throwing a coin...".format(i),
        result = random.randint(0, 1)
        if result == 0:
             print "It's a head!",
             heads += 1
        else:
            print "It's a tail!",
            tails += 1
        print "... Got {} head(s) so far and {} tail(s) so far".format(heads, tails)
    print "Ending the program. Thank you!"

coinTosses()