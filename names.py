# # Part I
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def names1(dict):
#     for i in dict:
#         print i['first_name'], i['last_name'] 

# names1(students)

# # Part II
users = {
 'Students': [
     {'first_name': 'Michael', 'last_name' : 'Jordan'},
     {'first_name': 'John', 'last_name' : 'Rosales'},
     {'first_name': 'Mark', 'last_name' : 'Guillen'},
     {'first_name': 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name' : 'Choi'},
     {'first_name': 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# def names2(dict):
#     for key, value in dict.iteritems():
#         print key
#         for i, _ in enumerate(value):
#             print i + 1, "=", dict[key][i]['first_name'].upper(), dict[key][i]['last_name'].upper(), "-",len(dict[key][i]['first_name'] + dict[key][i]['last_name'])

# names2(users)

def read_list(my_list):
    for value in my_list:
        counter = 0
        print value
        for item in my_list[value]:
            counter += 1
            first_name = item['first_name'].upper()
            last_name = item['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

read_list(users)