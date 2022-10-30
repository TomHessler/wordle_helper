from wordle_helper import grey, green, yellow

words = ['hello', 'phone','ghost','hallo','senap']

assert grey('a', words) == ['hello', 'phone','ghost']
assert grey('e', words) == ['ghost', 'hallo']
print('grey success')
assert yellow('e',1, words) == ['phone']
assert yellow('a',2, words) == ['hallo','senap']
print('yellow success')
assert green('e', 1, words) == ['hello','senap']
assert green('a', 2, words) == []
print('green success')