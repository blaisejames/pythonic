name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

def makingDictionaries(list1, list2):
    new_dict = {}
    new_dict = dict(zip(list1, list2))
    return new_dict

print(makingDictionaries(name, favorite_animal))

#Hacker Challenge: Oscar did not have a value and was dropped
print(makingDictionaries(name, favorite_animal2))