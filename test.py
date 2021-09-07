original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(original_list[0]['color'])

first_array = [1, 2, 3, 5, 7, 8, 9, 10]
test = lambda x: x in first_array

print(test(2))

orden = lambda x: 0 if x == 0 else -1/x
print(orden(1))

lista = [2, 3, 6, 1]
nueva_lista = sorted(lista, key = lambda x: x % 2 == 0)
print(lista)
print(nueva_lista)