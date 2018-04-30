# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print(words.find("day"))
month = words.replace("day", "month", 1) 
print(month)

# Min and Max
x = [2, 54, -2, 7, 12, 98]
print "Min: ", min(x)
print "Max: ", max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print "First: ", x[0]
print "Last: ", x[-1]

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[len(x)/2:]
y.insert(0, x[:len(x)/2])
print(y)
