from wordle_helper import grey, green, yellow
from optimal_word import get_optimal_guess, get_expected_outcome,simulate_guess

words = ['hello', 'phone','ghost','hallo','senap']

assert grey('a',None, words) == ['hello', 'phone','ghost']
assert grey('e',None, words) == ['ghost', 'hallo']
print('grey success')
assert yellow('e',1, words) == ['phone']
assert yellow('a',2, words) == ['hallo','senap']
print('yellow success')
assert green('e', 1, words) == ['hello','senap']
assert green('a', 2, words) == []
print('green success')

words = []

with open("wordtest.txt", encoding="UTF-8") as word_list_f:
    for word in word_list_f:
        words.append(word.strip('\n'))
    word_list_f.close()
print(get_optimal_guess(words))