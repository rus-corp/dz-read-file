file_name = "data.txt"

def book_reader(file_name):
  with open (file_name, encoding="utf-8") as file:
    cook_book = {}
    for line in file:
      dish_name = line.strip()
      foods = []
      quantity = file.readline()
      for item in range(int(quantity)):
        food = file.readline()
        foods.append(food.strip())
      cook_book[dish_name] = foods
        
      file.readline()
    return cook_book

    









print(book_reader(file_name))
