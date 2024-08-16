def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12)
print_params(12, 'hello')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [15, 'строчка', False]
values_dict = {'a': 11, 'b': True, 'c': 'привет'}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [20, 'список']
print_params(*values_list_2, 42)
