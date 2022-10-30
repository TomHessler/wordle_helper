from wordle_helper import grey, green, yellow

words = ['hello', 'phone','ghast','arise']

assert grey('a', words) == ['hello', 'phone']
assert grey('e', words) == ['ghast']
print('grey success')
assert yellow('e', words) == ['phone','arise']
assert yellow('a', words) == ['arise']
print('yellow success')
assert green('e', 1, words) == ['hello']
assert green('a', 2, words) == ['ghast']
print('green success')