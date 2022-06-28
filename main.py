# file_name = 'data.txt'

      
# def file_reader(file_name):
#     with open(file_name, encoding='utf-8') as file:
#         cook_book = {}
#         for line in file:
#             line = line.strip()
#             cook_book.update({line : []})
#             for item in range(int(file.readline().strip())):
#                 lst = file.readline().strip().split('|')
#                 dict = {'name':lst[0], 'quan':lst[1], 'mes': lst[2]}
#                 cook_book[line].append(dict)
#             file.readline()
#         return cook_book

# print(file_reader(file_name))

# cook_book = file_reader(file_name)


# def get_shop_list_by_dishes(dishes, person_count):
#   menu = {}
#   for k, v in cook_book.items():
#     if dishes == k:
#       for item in v:
#         menu1 = item.copy()
#         menu1['quan'] = menu1.get('quan') * person_count
#         x = menu1.get('name')
#         menu[x] = menu1
#   return (menu)

# print(get_shop_list_by_dishes('Омлет', 3))

file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
file4 = 'tot_file.txt'


def file_writen(file1, file4):
  with open(file1, encoding='utf8') as f1:
    for line in f1:
      print(line)  
  with open(file4, 'w', encoding='utf8') as f4:
    f4.writelines(line)
    for line2 in f4:
      print(line2)

print(file_writen(file1, file4))

# def file_writen(file1, file2, file3):
#   with open(file1, encoding='utf8') as file1:
#     f1 = len(file1.readlines())
#   with open(file2, encoding='utf8') as file2:
#     f2 = len(file2.readlines())
#   with open(file3, encoding='utf8') as file3:
#     f3 = len(file3.readlines())
#   with open(file4, 'w', 'encoding=utf8') as f4:
#     if f1 > f2 and f1 > f3:
#       f4.writelines(file2)
#       f4.writelines(file3)
#       f4.writelines(file1)
#     elif f1 > f2 and f1 < f3:
#       f4.writelines(file2)
#       f4.writelines(file1)
#       f4.writelines(file3)
#     elif f1 < f2 and f3 > f2:
#       f4.writelines(file1)
#       f4.writelines(file2)
#       f4.writelines(file3)

# print(file_writen(file1, file2, file3))



  