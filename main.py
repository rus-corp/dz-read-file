file_name = "data.txt"



def book_reader(file_name):
  open(file).read().split('\n')
  with open (file_name, encoding='utf8') as file:
    cook_book = {}
    for line in file:
      dish_name = line.strip()
      foods = []
      for item in range(int(file.readline())):
        food = file.readline().split(' | ')
        foods.append(food.split('\n'))
      cook_book[dish_name] = foods
      file.readline()
    return cook_book


print(book_reader(file_name))


