from tkinter import *

window = Tk()

def grey(letter, word_list):
    return [word for word in word_list if not letter in word]

def yellow(letter, word_list):
    return [word for word in word_list if letter in word]

def green(letter, index, word_list):
    return [word for word in word_list if word[index] == letter]

def get_result():
    text.delete(1.0,END)
    word_list = []
    with open('words.txt') as word_list_f:
        for word in word_list_f:
            word_list.append(word)
        word_list_f.close()
        
    green_letters = [entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get()]
    yellow_letters = entry_yellow.get()
    grey_letters = entry_grey.get()
    
    for index, green_letter in enumerate(green_letters):
        if green_letter:
            word_list = green(green_letter, index, word_list)
            
    for yellow_letter in yellow_letters:
        word_list = yellow(yellow_letter, word_list)
        
    for grey_letter in grey_letters:
        word_list = grey(grey_letter, word_list)

    words = ''
    
    for word in word_list:
        words += word

    text.insert(END, words)

window.title('Wordle Helper')
window.geometry("400x600")

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

label1 = Label(window, text="Enter letters in correct positions:",font = ('Verdana',15))
label1.place(x=30,y=10)

label2 = Label(window, text="Enter yellow letters:",font = ('Verdana',15))
label2.place(x=95,y=110)

entry_yellow = Entry(window,bg="yellow",font = ('Verdana',30))
entry_yellow.place(x=50,y=150,width=300,height=50)

label3 = Label(window, text="Enter grey letters:",font = ('Verdana',15))
label3.place(x=100,y=210)

entry_grey = Entry(window,bg="grey",font = ('Verdana',30))
entry_grey.place(x=50,y=250,width=300,height=50)
    

button = Button(window,width=7,height=1,text ="Get Words",command = get_result)
button.place(x=173,y=350)

text = Text(window)
text.place(x=50,y=420,width=300,height=160)

window.mainloop()