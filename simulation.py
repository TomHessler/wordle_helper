from wordle_helper import grey, yellow, green, suggest_word

def result(guess, answer):
    result = []
    for index, letter in enumerate(guess):
        if letter not in answer:
            result.append(grey)
        elif answer[index] == letter:
            result.append(green)
        else:
            result.append(yellow)
    return result


def simulate_game(answer, word_list):
    trials = 1
    while len(word_list)>1:
        trials +=1
        guess = suggest_word(word_list).strip('\n')
        color_list = result(guess, answer)
        for index, color in enumerate(color_list):
            word_list = color(guess[index], index, word_list)
    return trials


def simulation(word_list, answer_list):    
    total = 0
    
    for answer in answer_list:
        total += simulate_game(answer, word_list)
    
    avg_number_guesses = total/len(answer_list)
    return avg_number_guesses


if __name__ == '__main__':
    
    answer_list = []
    word_list = []
    
    with open("words.txt", encoding="UTF-8") as word_list_f:
        for word in word_list_f:
            answer_list.append(word)
        word_list_f.close()
        
    with open("all_words.txt", encoding="UTF-8") as word_list_f:
        for word in word_list_f:
            word_list.append(word)
        word_list_f.close()
        
    print(f'average number of guesses without knowing answer list: {simulation(word_list, answer_list)}')
    print(f'average number of guesses given answer list: {simulation(answer_list, answer_list)}')