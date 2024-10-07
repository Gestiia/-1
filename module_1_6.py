my_dict = {'Olga': 1989, 'Pavel': 1965, 'Roma': 1947 }
print('Список: ', my_dict)
print('Ольга: ', my_dict['Olga'])
print('Марина: ', my_dict.get('Marina'))
my_dict.update({'Denis': 2002,
                'Tomara': 2010})
delete = my_dict.pop('Roma')
print('Рома больше не с нами: ', delete)
print(my_dict)

my_set = {210, 111, 456, 156}
print(my_set)
my_set.add(555), my_set.add('hot')
my_set.remove(210)
print(my_set)
