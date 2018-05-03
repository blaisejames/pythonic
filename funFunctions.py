# Odd/Even
def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print 'Number is {}. This is an even number.'.format(i)
        else:
            print 'Number is {}. This is an odd number.'.format(i)

odd_even()    

# Multiply
def multiply(a, b):
    new_list = []
    new_list = [b * i for i in a]
    return new_list

print (multiply([2,4,10,16], 5))

# Hacker Challenge
def layered_multiples(arr):
    new_array = [] 
    for i in arr:
        new_array.append([1]*i) 
    return new_array

print(multiply([2,4,5],3))
print(layered_multiples(multiply([2,4,5],3)))