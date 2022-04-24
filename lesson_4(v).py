# dict_data = {
#     'name': 'Vadim',
#     'age': 32,
#     'weight': 94,
#     'food': {'milk':['Srnchki', 'milk', 'protein', 'tvorog'],
#              'meat':['pelmeni', 'meat', 'sosiska v teste']},
#     'salary': [250, 320, 700, 1100,1200,1500,2000]}    - это словарь в котором есть ключи (нэйм, фуд, эйдж и т.д) и данные - вадим, 32, 94 и проч.
#
# key_list = []
#
# for key, value in dict_data.items():        - данный цикл обращается и к ключам (key) и к данным (value). А dict.data.items() отвечает за перебор всех данных
#     if key == 'food':
#         key_list = value['milk']
#
#     # key_list.append(value)
#     # print(key,'==', value)
#
#
# print('======================')
# print(key_list)
#
# for i in key_list:
#     print(i)
#
#






# dict_data = {
#     'name': 'Vadim',
#     'age': 32,
#     'weight': 94,
#     'food': {'milk':['Srnchki', 'milk', 'protein', 'tvorog'],
#              'meat':['pelmeni', 'meat', 'sosiska v teste']},
#     'salary': [250, 320, 700, 1100,1200,1500,2000]}
#
# key_list = []
#
# for key, value in dict_data.items():
#     if key == 'food':
#         key_list = value['milk']
#
#     # key_list.append(value)
#     # print(key,'==', value)
#
#
# print('======================')
# print(key_list)
#
# for i in key_list:
#     print(i)



# def ff(n):
#     return n*2
#
# items_list = [ff(i) for i in range (0,10) if i%2 == 0 and i % 4 == 0 ]
# print(items_list)
#
# items_list_2 = []
#
# for ii in range(0,10):
#     items_list_2.append(ii)
# print(items_list)




import time


while True:
    input_value  = input('input your value: ')
    if type (int(input_value)) != int:
        print('Enter int please')
        continue

    nn = int(input_value) * 2
    print('You value x2 =', nn)
    if nn  > 100:
        break