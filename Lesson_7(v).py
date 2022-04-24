file_path = 'C:\Users\nedvi\OneDrive\Рабочий стол\itproger\text\'


text_file_title = 'text_2.txt'

file_title = file_path + text_file_title

# 'w' //.write - записать что-либо в текстовом файле
# 'a' //.append - добавить что-либо в текстовый файл
# 'r' //.read - прочитать текстовый файл
# 'r+' // - прочесть что-либо в файле с возможностью записи





# file_title = file_path + text_file_title
#
# ll = ['qa', 'autonation', 'miserable']
#
# with open(file_title, 'a', encoding='utf-8') as f:
#     # f.write('Goddamnit')
#     # f.writelines(ll)
#     # f.writelines(ll)
#     # f.writelines('\n'.join(ll))
#
#     for n in range(0,10):
#         for i in ll:
#           # f.write(i)
#           # f.write('\n')
#              w_line = str(n) + '_' + i
#              f.writelines(w_line)
#              f.write('\n')



with open(file_title, 'r', encoding='utf-8') as f:

    ff = f.readlines()
    print(ff)
    del ff[1]

    with open(file_title, 'w', encoding='utf-8') as wf:
        f.writelines(ff)
    # print(len(ff)) - функция len демонстрирует кол-во данный через запятую


