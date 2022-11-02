from wordle_helper import suggest_word, result
import matplotlib.pyplot as plt

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
    trials_list = {}
    for answer in answer_list:
        trials, fails, failed_answer = simulate_game(answer, word_list)
        total_trails += trials
        trials_list[answer] = trials
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
    max_try_answers = []
    for answer, trials in trials_list.items():
        if trials == 6:
            max_try_answers.append(answer)
    print(f"average number of guesses: {avg_number_guesses}")
    print(f"success rate: {success_rate}")
    print(f'max tries: {max_try_answers}')
    print(f"failed answers: {failed_answers_clean}")
    number_trials = [i+1 for i in range(6)]
    tries_count = [0 for i in range(6)]
    for trials in trials_list.values():
        tries_count[trials-1] +=1
    plt.bar(number_trials,tries_count)
    plt.xlabel("Guesses")
    plt.show()