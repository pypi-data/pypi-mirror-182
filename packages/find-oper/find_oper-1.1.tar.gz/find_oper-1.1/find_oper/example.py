"""example module"""

from find_operators import find

print('example 1')
phone_operator_regions_1 = {'O!': {4, 5, 7, 9},
                            'Мегаком': {1, 2, 3, 4, 5, 6},
                            'Билайн': {1, 4, 5, 10, 11}}
regions_1 = {1, 2, 3, 4, 5, 7, 11}
print(phone_operator_regions_1, regions_1,)
print(find(phone_operator_regions_1, regions_1))

print('example 2')
phone_operator_regions_2 = {'O!': {4, 5, 7, 9},
                            'Мегаком': {1, 2, 3, 4, 5, 6},
                            'Билайн': {1, 4, 5, 10, 11}}
regions_2 = {1, 2, 3, 4, 5, 7, 77}
print(phone_operator_regions_2, regions_2)
print(find(phone_operator_regions_2, regions_2))

print('example 3')
phone_operator_regions_3 = {'Билайн': {1, 5, 19, 77, 1001},
                            'O!': {2, 3, 4, 5, 6, 7},
                            'Мегаком': {1, 3, 5, 177}}
regions_3 = {2, 5, 6, 7, 77, 177, 1001}
print(phone_operator_regions_3, regions_3)
print(find(phone_operator_regions_3, regions_3))
