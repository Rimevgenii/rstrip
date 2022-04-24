import csv
import json

file_name = '/Users/nedvi/OneDrive/Рабочий стол/itproger/newjson.json'


users = {}
users = {1:'Vadim',
         2:'Irina',
         'name':'Alex'}


users2 = {1:'Vadim',
          2:'Irina',
          3: ['Alex', 'Olga', 'Victory']}

users3 = {1:'Vadim',
          2:'Irina',
          3: users}

users4 = {1:'Vadim',
          2:'Irina',
          3: {'name': 'George',
              'age': 30,
              'height': 178,
              'Family':{'children':['Anna','Alex']}}}

users4[3]['age'] = 40
# users4[3]['age'] = 40 - замена value в дикте

users4.pop(2)
# users4.pop(2) - удаление ключа по индексу (ирина)

users4[2] = 'ignat'
# users4[2] = 'ignat' - создание нового ключа взамен удаленного
#                     с прописанием к нему value



# users4.clear() - полная зачистка словаря и данных
# users4.popitem() - метод удаляет последний ключ и его данные
# print(len(users4)) - отображает количество ключей в словаре
# xx = users4.copy() - копия указанного элемента

name = ('Vadim', 'Misha','Alex')
age = 30, 20, 40

users44 = dict.fromkeys(name, age)
# users44 = dict.fromkeys(name, age) - создана новая переменная в которой срабатывает функция fromkeys в которую мы подставляем ключи и вэльюсы.

# print(users44)
u_4 = {}

for i in range (0, len(name)):
    u_4[name[i]] = age[i]

print(u_4)

with open(file_name, 'w') as jf:
    json.dump(u_4, jf)


with open(file_name, 'r') as r:
    data = r.read()
    js_obj = json.loads(data)

    print(js_obj)