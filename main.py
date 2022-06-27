file_name = 'data.txt'

# def open_file(file_name):
#   with open(file_name, encoding='utf8') as file:
#     return file.read().strip().split('\n\n')


# file_show = open_file('data.txt')


# def cook_book (dish_menu):
#   for item in dish_menu:
#     res = item.split('\n')
#     for i in res[2:]:
#       ras = i.split(' | ')
#       # print(ras)
#       cook_book = {res[0]:{'name': ras[0], 'quan': ras[1], 'mesu': ras[2]}}
#       print(cook_book)
    
      
# cook_book(file_show)
def file_reader(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line : []})
            for item in range(int(file.readline().strip())):
                lst = file.readline().strip().split('|')
                dict = {'name':lst[0], 'quan':lst[1], 'mes': lst[2]}
                cook_book[line].append(dict)
            file.readline()
        return cook_book

print(file_reader(file_name))





# print(book_reader(file_name))


# cook_book = {res[0]:{'name': ras[0], 'quan': ras[1], 'mesu': ras[2]}}
#     print(cook_book)
