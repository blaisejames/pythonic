# Multiples
# Part I -- prints odd numbers from 1 to 1000
for x in range(1, 1000, 2):
    print(x)

# Part II -- prints the multiples of 5 from 5 to 1 million
for x in range(5, 1000005, 5):
    print(x)

# Sum List -- prints the sum of all the values in the list
a = [1, 2, 5, 10, 255, 3]
print(sum(a))

''' 
Alternative Approach
a = [1, 2, 5, 10, 255, 3
# sum = 0
# for x in a:
#     sum += x
# print(sum) 
'''

# Avg List -- prints the average of the values in the list
a = [1, 2, 5, 10, 255, 3]
print (sum(a)/len(a))