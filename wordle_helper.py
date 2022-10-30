from tkinter import *

def grey(letter, word_list):
    return [word for word in word_list if not letter in word]

# def yellow(letter, word_list):
#     return [word for word in word_list if letter in word]

def yellow(letter, index, word_list):
    new_list = [word for word in word_list if letter in word]
    return [word for word in new_list if not word[index] == letter]

def green(letter, index, word_list):
    return [word for word in word_list if word[index] == letter]

def get_result():
    text.delete(1.0,END)
    word_list = []
    with open('words.txt') as word_list_f:
        for word in word_list_f:
            word_list.append(word)
        word_list_f.close()
        
    green_letters = [entry1.get().strip(),entry2.get().strip(),entry3.get().strip(),entry4.get().strip(),entry5.get().strip()]
    # yellow_letters = entry_yellow.get().strip()
    yellow_letters = [entry6.get().strip(),entry7.get().strip(),entry8.get().strip(),entry9.get().strip(),entry10.get().strip()]
    grey_letters = entry_grey.get().strip()
    
    for index, green_letter in enumerate(green_letters):
        if green_letter:
            word_list = green(green_letter, index, word_list)
            
    # for yellow_letter in yellow_letters:
    #     word_list = yellow(yellow_letter, word_list)
    
    for index, yellow_letter in enumerate(yellow_letters):
        if yellow_letter:
            for letter in yellow_letter:
                word_list = yellow(letter, index, word_list)
        
    for grey_letter in grey_letters:
        word_list = grey(grey_letter, word_list)

    words = ''
    
    for word in word_list:
        words += word
        
    label_count_words.config(text=f"Number of possible answers: {len(word_list)}",font = ('Verdana',10))
    
    text.insert(END, words)

def GUI():

    window = Tk()
    
    window.title('Wordle Helper')
    window.geometry("400x600")
    
    label1 = Label(window, text="Enter letters in correct positions:",font = ('Verdana',15))
    label1.place(x=30,y=10)
    
    entry1 = Entry(window,bg="green",font = ('Verdana',30))
    entry2 = Entry(window,bg="green",font = ('Verdana',30))
    entry3 = Entry(window,bg="green",font = ('Verdana',30))
    entry4 = Entry(window,bg="green",font = ('Verdana',30))
    entry5 = Entry(window,bg="green",font = ('Verdana',30))
    
    entry1.place(x=100-25,y=50,width=50,height=50)
    entry2.place(x=150-25,y=50,width=50,height=50)
    entry3.place(x=200-25,y=50,width=50,height=50)
    entry4.place(x=250-25,y=50,width=50,height=50)
    entry5.place(x=300-25,y=50,width=50,height=50)
    
    label2 = Label(window, text="Enter yellow letters:",font = ('Verdana',15))
    label2.place(x=90,y=110)
    
    entry6 = Entry(window,bg="yellow",font = ('Verdana',30))
    entry7 = Entry(window,bg="yellow",font = ('Verdana',30))
    entry8 = Entry(window,bg="yellow",font = ('Verdana',30))
    entry9 = Entry(window,bg="yellow",font = ('Verdana',30))
    entry10 = Entry(window,bg="yellow",font = ('Verdana',30))
    
    entry6.place(x=100-25,y=150,width=50,height=50)
    entry7.place(x=150-25,y=150,width=50,height=50)
    entry8.place(x=200-25,y=150,width=50,height=50)
    entry9.place(x=250-25,y=150,width=50,height=50)
    entry10.place(x=300-25,y=150,width=50,height=50)
    
    # entry_yellow = Entry(window,bg="yellow",font = ('Verdana',30))
    # entry_yellow.place(x=50,y=150,width=300,height=50)
    
    label3 = Label(window, text="Enter grey letters:",font = ('Verdana',15))
    label3.place(x=100,y=210)
    
    entry_grey = Entry(window,bg="grey",font = ('Verdana',30))
    entry_grey.place(x=50,y=250,width=300,height=50)
        
    
    button = Button(window,width=8,height=1,text ="Get Words",command = get_result)
    button.place(x=165,y=325)
    
    text = Text(window)
    text.place(x=50,y=380,width=300,height=185)
    
    scrollbar = Scrollbar(orient=VERTICAL)
        
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=335,y=380,height=180)
    
    label_count_words = Label(window)
    label_count_words.place(x=50,y=570)
    
    window.mainloop()
    
if __name__ == '__main__':
    GUI()