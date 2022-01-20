from distutils import command
from random import *
import nltk
from nltk.tag.mapping import tagset_mapping
from nltk.tokenize import word_tokenize
from tkinter import *
from tkinter.ttk import Combobox  
from tkinter import scrolledtext
from tkinter import messagebox 

# сохранется всё книги в переменную 
books = open("100-Ways-To-Motivate-Others-1.txt",encoding="utf8").read() + open("100-Ways-to-Motivate-Yourself-Change-Your-Life-Forever.txt",encoding="utf8").read() + open("Most-populars-words.txt",encoding="utf8").read()
books_word = word_tokenize(books)

word_tags = (nltk.pos_tag((books_word), tagset="universal"))

noun_dict = []
verb_dict = []
adjective_dict = [] #пустые списки для сущ, глагола, прилагательного

def Word_Noun():
    global word_noun
    for x in word_tags:
        if x[1] == "NOUN":
            noun_dict.append(x[0])
    
    noun_dict_range = len(noun_dict)
    noun_id = randint(0,noun_dict_range)
    word_noun = noun_dict[noun_id]
    
def Word_Verb():
    global word_verb
    for x in word_tags:
        if x[1] == "VERB":
            verb_dict.append(x[0])
    
    verb_dict_range = len(verb_dict)
    verb_id = randint(0,verb_dict_range)
    word_verb = verb_dict[verb_id]

def Word_Adjective():
    global word_adjective
    for x in word_tags:
        if x[1] == "ADJ":
            adjective_dict.append(x[0])
    
    adjective_dict_range = len(adjective_dict)
    adjective_id = randint(0,adjective_dict_range)
    word_adjective = adjective_dict[adjective_id]

def first_group():
    answer = word_verb
    return answer

def second_group():
    answer = word_verb +" " + word_noun
    answer2 = word_verb + " " + word_adjective

    x = randint(0,1)
    if x == 0:
        return answer
    elif x == 1:
         return answer2

def third_group():
    answer = word_noun + " is " + word_adjective
    return answer

def fourth_group():
    global name
    name = ''
    name = company
    answer = name + " is " + word_adjective
    return answer

def btnGroup(answer):
    if answer == 1:
        Word_Verb()
        txt.delete(1.0,END)
        txt.insert(INSERT,first_group())
    elif answer == 2:
        Word_Verb()
        Word_Adjective()
        Word_Noun()
        txt.delete(1.0,END)
        txt.insert(INSERT,second_group())
    elif answer == 3:
        Word_Adjective()
        Word_Noun()
        txt.delete(1.0,END)
        txt.insert(INSERT,third_group())
    elif answer == 4:
        global company
        company = display.get()
        Word_Adjective()
        Word_Noun()
        txt.delete(1.0,END)
        txt.insert(INSERT,fourth_group())

    return None

def clear():
    display.delete(0, END)
    return None

def helpm():  
    messagebox.showinfo('Help', '''Lai izveidotu saukļu, noklikšķiniet uz vienas no pogām
    1. Noklikšķinot uz pogas "1.grupa", tiks ģenerēts saukļus pēc veidnes: "Darbības vārds"
    2. Noklikšķinot uz pogas "2.grupa", tiks ģenerēts saukļis pēc veidnes: "Darbības vārds + lietvārds vai darbības vārds + īpašības vārds"
    3. Noklikšķinot uz pogas "3.grupa", tiks ģenerēts saukļus pēc veidnes: "Lietvārds + darbības vārds “is” + īpašības vārds"
    4. Noklikšķinot uz pogas "4.grupa", tiks ģenerēts saukļus pēc veidnes: "Uzņēmuma nosaukums (vai vārds) + darbības vārds “is” + īpašības vārds", lai uzrakstītu uzņēmuma nosaukumu, ievadiet to zemāk rozā laukā''') 

m_vizual = Tk()
m_vizual.title("MIGENERATOR")
m_vizual.geometry('700x500')
m_vizual.configure(bg = "#CDB4DB")

display = Entry(m_vizual,font = ("Helvetica",15),width=35, bg= "#F09ACD" )
display.grid(row=3, columnspan=2,column=1)
btn_check = Button(m_vizual,text="Clear",font = ("Helvetica",11), command = clear, bg = "#FFC08C")
btn_check.grid(row=3,column=3)

lbl_discription = Label(m_vizual,text='Sveiki! Tas ir "Automātiskā reklāmas saukļu ģenerators"' ,font = ("Helvetica",15), bg = "#FFC08C")
lbl_discription.grid(row=0,columnspan=4, )

btn1 = Button(m_vizual, text = "1.grupa", padx = 10, pady = 20, font = ("Helvetica",15),command = lambda:btnGroup(1), bg = "#FFC08C")
btn2 = Button(m_vizual, text = "2.grupa", padx = 10, pady = 20, font = ("Helvetica",15),command = lambda:btnGroup(2), bg = "#FFC08C")
btn3 = Button(m_vizual, text = "3.grupa", padx = 10, pady = 20, font = ("Helvetica",15),command = lambda:btnGroup(3), bg = "#FFC08C")
btn4 = Button(m_vizual, text = "4.grupa", padx = 10, pady = 20, font = ("Helvetica",15),command = lambda:btnGroup(4), bg = "#FFC08C")

btn1.grid(row = 1,column=0)
btn2.grid(row = 1,column=1)
btn3.grid(row = 1,column=2)
btn4.grid(row = 1,column=3)

btn_help = Button(m_vizual,text="Help!",padx = 10, pady = 20, font = ("Helvetica",30), command=helpm, bg = "#FFC08C" )
btn_help.grid(row=4,columnspan=4)

txt = scrolledtext.ScrolledText(m_vizual, width=62, height=10,font = ("Helvetica",15))  
txt.grid(columnspan=4, row=2)


m_vizual.mainloop()