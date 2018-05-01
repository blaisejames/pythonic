l = ['magical unicorns', 19, True, ["a","b","c"], 'hello', 98.98, 'world', 31]
tot, flo, boo, string, lst, typ = 0, 0, [], "", [], set()

for x in l:
    print x, "is", type(x)

    if isinstance(x, int):
        tot += x
        typ.add('int')
    if isinstance(x, float):
        flo += x
        typ.add('float')
    if isinstance(x, bool):
        boo.append(str(x))
        typ.add('boo')
    if isinstance(x, str):
        string = string + " " + x
        typ.add('str')
    if isinstance(x, list):
        lst.append(x)
        typ.add('list')
if len(typ) > 1:
    print "\nThe list you entered is of mixed type"
else:
    print "The list you entered is of", type(x)
if tot > 0:
    print "Int Sum:", tot
if flo > 0:
    print "Float Sum:", flo
if len(boo) > 0:
    print "Bool:", boo
if len(string) > 0:
    print "String:", string 
if len(lst) > 0:
    print "List:", lst 
