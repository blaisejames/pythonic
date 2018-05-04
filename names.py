# Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(dict):
    for i in dict:
        print i['first_name'], i['last_name'] 

names(students)

# Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(dict):
    for k, v in dict.iteritems():
        print k
        for i, _ in enumerate(v):
            print i + 1, "=", dict[k][i]['first_name'].upper(), dict[k][i]['last_name'].upper(), "-", len(dict[k][i]['first_name'] + dict[k][i]['last_name'])

names(users)