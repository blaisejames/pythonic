me = {'name': 'Blaise', 'age': 'over 35', 'country': 'The United States', 'language': 'Python'}

def dictionaryBasics(dict):
    for k, v in dict.items():
        print "My {} is {}".format(k, v)

dictionaryBasics(me)