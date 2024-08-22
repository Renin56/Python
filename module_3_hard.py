data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    ts = 0
    tl = 0

    for i in data:
        if isinstance(i, int):
            ts += i
        elif isinstance(i, str):
            ts += len(i)
        elif isinstance(i, list):
            ts += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                tl += len(key)
            ts += tl + calculate_structure_sum(list(i.values()))
        elif isinstance(i, (tuple, set)):
            ts += calculate_structure_sum(i)
    return ts


total_sum = calculate_structure_sum(data_structure)
print(f'Сумма всех элементов: {total_sum}')