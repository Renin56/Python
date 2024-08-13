calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    c = ()
    c = (len(string), string.upper(), string.lower())
    count_calls()
    return c

def is_contains(string, list_to_search):
    res = False

    for i in list_to_search:
        if string.lower() == i.lower():
            res = True
            break
        else:
            res = False
    count_calls()
    return res


print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
