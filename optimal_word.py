from simulation import result

def get_optimal_guess(word_list):
    expected_outcome_for_word = {}
    for word in word_list:
        expected_outcome_for_word[word] = get_expected_outcome(word, word_list)
    return min(expected_outcome_for_word, key=expected_outcome_for_word.get)

def simulate_guess(guess, word_list, answer):
    color_list = result(guess, answer)
    for index, color in enumerate(color_list):
        word_list = color(guess[index], index, word_list)
    return len(word_list)

def get_expected_outcome(guess, word_list):
    total = 0
    for answer in word_list:
        if not answer == guess:
            total += simulate_guess(guess, word_list, answer)
    return total / len(word_list)