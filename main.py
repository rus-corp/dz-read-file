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
#       cook_book = {res[0]:{'name': ras[0], 'quan': ras[1], 'mesu': ras[2]}}
#       print(cook_book)




# cook_book(file_show)

def book_reader(file_name):
  with open (file_name, encoding='utf8') as file:
    cook_book = {}
    for line in file:
      dish_name = line.strip()
      foods = []
      for item in range(int(file.readline())):        
        food = file.readline().split(' | ')
        food = [line.rstrip() for line in food]
        
        foods.append(food)
        
        
      cook_book[dish_name] = foods
      file.readline()
    return cook_book


print(book_reader(file_name))



