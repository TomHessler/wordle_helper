import tkinter as tk


def grey(letter, word_list):
    return [word for word in word_list if not letter in word]


def yellow(letter, index, word_list):
    new_list = [word for word in word_list if letter in word]
    return [word for word in new_list if not word[index] == letter]


def green(letter, index, word_list):
    return [word for word in word_list if word[index] == letter]

def all_unique(word):
    word = sorted(word)
    for i in range(len(word)-1):
        if (word[i] == word[i + 1]) :
            return False
         
    return True


def return_distinct_five_letter_words(word_list):
    new_list = []
    for word in word_list:
        if all_unique(word):
            new_list.append(word.strip('\n'))
    return new_list

def count_letters(word_list):
    count = {}
    for word in word_list:
        for letter in word.strip('\n'):
            if letter in count.keys():
                count[letter] += 1
            else:
                count[letter] = 1
    return count
        
def rank_words(word_list):
    letter_count = count_letters(word_list)
    word_ranking = {word:0 for word in word_list}
    for word in word_list:
        for letter in word.strip('\n'):
            word_ranking[word] += letter_count[letter]
    return dict(sorted(word_ranking.items(), key=lambda item: item[1]))


def suggest_word(word_list):
    word_ranking = rank_words(return_distinct_five_letter_words(word_list))
    return list(word_ranking.keys())[-1]


def get_result(event=None):
    text.delete(1.0, tk.END)
    word_list = []
    with open("words.txt", encoding="UTF-8") as word_list_f:
        for word in word_list_f:
            word_list.append(word)
        word_list_f.close()

    green_letters = [
        entry1.get().strip().lower(),
        entry2.get().strip().lower(),
        entry3.get().strip().lower(),
        entry4.get().strip().lower(),
        entry5.get().strip().lower(),
    ]

    yellow_letters = [
        entry6.get().strip().lower(),
        entry7.get().strip().lower(),
        entry8.get().strip().lower(),
        entry9.get().strip().lower(),
        entry10.get().strip().lower(),
    ]
    grey_letters = entry_grey.get().strip().lower()

    for index, green_letter in enumerate(green_letters):
        if green_letter:
            word_list = green(green_letter, index, word_list)

    for index, yellow_letter in enumerate(yellow_letters):
        if yellow_letter:
            for letter in yellow_letter:
                word_list = yellow(letter, index, word_list)

    for grey_letter in grey_letters:
        word_list = grey(grey_letter, word_list)

    label_count_words.config(
        text=f"Number of possible answers: {len(word_list)}", font=("Verdana", 10)
    )
    
    label_suggested_word.config(
        text=f"Suggested guess: {suggest_word(word_list)}", font=("Verdana", 10)
    )
    
    text.insert(tk.END, "".join(word_list))


def reset():
    entry1.delete(0, "end")
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    entry5.delete(0, "end")
    entry6.delete(0, "end")
    entry7.delete(0, "end")
    entry8.delete(0, "end")
    entry9.delete(0, "end")
    entry10.delete(0, "end")
    entry_grey.delete(0, "end")
    text.delete(1.0, tk.END)
    label_count_words.config(text="")
    label_suggested_word.config(text="")


if __name__ == "__main__":
    window = tk.Tk()

    window.title("Wordle Helper")
    window.geometry("400x610")

    label1 = tk.Label(
        window, text="Enter letters in correct positions:", font=("Verdana", 15)
    )
    label1.place(x=30, y=10)

    entry1 = tk.Entry(window, bg="green", font=("Verdana", 30))
    entry2 = tk.Entry(window, bg="green", font=("Verdana", 30))
    entry3 = tk.Entry(window, bg="green", font=("Verdana", 30))
    entry4 = tk.Entry(window, bg="green", font=("Verdana", 30))
    entry5 = tk.Entry(window, bg="green", font=("Verdana", 30))

    entry1.place(x=100 - 25, y=50, width=50, height=50)
    entry2.place(x=150 - 25, y=50, width=50, height=50)
    entry3.place(x=200 - 25, y=50, width=50, height=50)
    entry4.place(x=250 - 25, y=50, width=50, height=50)
    entry5.place(x=300 - 25, y=50, width=50, height=50)

    label2 = tk.Label(window, text="Enter yellow letters:", font=("Verdana", 15))
    label2.place(x=90, y=110)

    entry6 = tk.Entry(window, bg="yellow", font=("Verdana", 30))
    entry7 = tk.Entry(window, bg="yellow", font=("Verdana", 30))
    entry8 = tk.Entry(window, bg="yellow", font=("Verdana", 30))
    entry9 = tk.Entry(window, bg="yellow", font=("Verdana", 30))
    entry10 = tk.Entry(window, bg="yellow", font=("Verdana", 30))

    entry6.place(x=100 - 25, y=150, width=50, height=50)
    entry7.place(x=150 - 25, y=150, width=50, height=50)
    entry8.place(x=200 - 25, y=150, width=50, height=50)
    entry9.place(x=250 - 25, y=150, width=50, height=50)
    entry10.place(x=300 - 25, y=150, width=50, height=50)

    label3 = tk.Label(window, text="Enter grey letters:", font=("Verdana", 15))
    label3.place(x=100, y=210)

    entry_grey = tk.Entry(window, bg="grey", font=("Verdana", 30))
    entry_grey.place(x=50, y=250, width=300, height=50)

    text = tk.Text(window)
    text.place(x=50, y=380, width=300, height=185)

    scrollbar = tk.Scrollbar(orient=tk.VERTICAL)

    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=335, y=380, height=185)

    label_count_words = tk.Label(window)
    label_count_words.place(x=50, y=565)
    
    label_suggested_word = tk.Label(window)
    label_suggested_word.place(x=50, y=585)

    button = tk.Button(window, width=8, height=1, text="Get Words", command=get_result)
    button.place(x=200 + 10, y=325)

    reset_button = tk.Button(window, width=8, height=1, text="Reset", command=reset)
    reset_button.place(x=100 + 10, y=325)

    window.bind("<Return>", get_result)

    window.mainloop()
