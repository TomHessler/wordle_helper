from wordle_helper import suggest_word, result

def simulate_game(answer, word_list):
    trials = 0
    fails = 0
    failed_answer = ''
    while True:
        trials += 1
        if trials>6:
            fails += 1
            failed_answer = answer
            break
        guess = suggest_word(word_list).strip("\n")
        if guess == answer.strip('\n'):
            break
        color_list = result(guess, answer)
        for index, color in enumerate(color_list):
            word_list = color(guess[index], index, word_list)
    return trials, fails, failed_answer


def simulation(word_list, answer_list):
    total_trails = 0
    total_fails = 0
    failed_answers = []
    trials_list = []
    for answer in answer_list:
        trials, fails, failed_answer = simulate_game(answer, word_list)
        total_trails += trials
        trials_list.append(trials)
        total_fails += fails
        failed_answers.append(failed_answer)
    avg_number_guesses = total_trails / len(answer_list)
    success_rate = 1 - total_fails / len(answer_list)
    return avg_number_guesses, success_rate, failed_answers, trials_list


if __name__ == "__main__":

    answer_list = []
    word_list = []

    with open("data/words.txt", encoding="UTF-8") as word_list_f:
        for word in word_list_f:
            answer_list.append(word)
        word_list_f.close()

    avg_number_guesses, success_rate, failed_answers, trials_list = simulation(answer_list, answer_list)
    failed_answers_clean = []
    for answer in failed_answers:
        if answer:
            failed_answers_clean.append(answer.strip('\n'))
    count_max_trials = 0
    for nr_trials in trials_list:
        if nr_trials == 6:
            count_max_trials += 1
    print(f"average number of guesses: {avg_number_guesses}")
    print(f"success rate: {success_rate}")
    print(f'max tries: {max(trials_list)}')
    print(f'number of times 6 tries was needed: {count_max_trials}')
    print(f"failed answers: {failed_answers_clean}")