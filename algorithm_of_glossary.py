my_file = open('iv.txt', 'r', encoding='utf-8')

#### add a new empty list (for generate a glossary)
a = [] # class 'list'
key = [] # #class 'list'

#### add data from file txt in empty list a
for i in my_file:
    a.append(i)

#### filling list key (for generate a dictionary)
for el_2 in a:
    key.append(el_2)

dictionary = dict(zip(a, key))   # creat a dictionary by method ZIP  (combining 2 dictionaries 'a' and 'key')

print(dictionary['be [bi:]\twas [wɔz], were [wз:]\tbeen [bi:n]\tбыть\n'])
print(type(dictionary))




