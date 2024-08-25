calls = 0


def count_call():
    global calls
    calls = calls + 1


def string_info(string):
    count_call()
    up = string
    down = string
    return (len(string), up.upper(), down.lower())


def is_contains(string, is_contains):
    count_call()
    return 'Urban' in (string, is_contains)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
