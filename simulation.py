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
    trials = 0
    fails = 0
    while True:
        trials += 1
        if trials>6:
            fails += 1
            break
        guess = suggest_word(word_list).strip("\n")
        if guess == answer.strip('\n'):
            break
        color_list = result(guess, answer)
        for index, color in enumerate(color_list):
            word_list = color(guess[index], index, word_list)
    return trials, fails


def simulation(word_list, answer_list):
    total_trails = 0
    total_fails = 0
    for answer in answer_list:
        trials, fails = simulate_game(answer, word_list)
        total_trails += trials
        total_fails += fails
    avg_number_guesses = total_trails / len(answer_list)
    success_rate = 1 - total_fails / len(answer_list)
    return avg_number_guesses, success_rate


if __name__ == "__main__":

    answer_list = []
    word_list = []

    with open("words.txt", encoding="UTF-8") as word_list_f:
        for word in word_list_f:
            answer_list.append(word)
        word_list_f.close()

    avg_number_guesses, success_rate = simulation(answer_list, answer_list)

    print(f"average number of guesses: {avg_number_guesses}")
    print(f"success rate: {success_rate}")