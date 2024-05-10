# people=['Elisabeth','Steven','Sebastian','Margaret','Svietlana','Raphael']

# domain = 'mycompany.com'
# for person in people:
#     email = person + '@' + domain
#     print('Email for\t', person, '\tis\t', email)
# else:
#     print('-- end of the list--')

#zad2

# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']

# for line in data:
#     print(line.upper())

#zad 3

# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']

# for line in data:
#     elements = line.split(':')
#     print(elements[0].upper())
#     print(elements[1])

# zad 4

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for line in data:
    elements = line.split(':')
    if elements[0]=='Error':
        print(elements[1].upper())
    else:
        print(elements[1])