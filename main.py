file_name = 'data.txt'

      
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

cook_book = file_reader(file_name)


def get_shop_list_by_dishes(dishes, person_count):
  menu = {}
  for k, v in cook_book.items():
    if dishes == k:
      for item in v:
        menu1 = item.copy()
        menu1['quan'] = menu1.get('quan') * person_count
        x = menu1.get('name')
        menu[x] = menu1
  return (menu)

print(get_shop_list_by_dishes('Омлет', 3))




  