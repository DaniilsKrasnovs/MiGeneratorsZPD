import eel
from random import *
import nltk
from nltk.tag.mapping import tagset_mapping
from nltk.tokenize import word_tokenize

books = open("100-Ways-To-Motivate-Others-1.txt",encoding="utf8").read() + open("100-Ways-to-Motivate-Yourself-Change-Your-Life-Forever.txt",encoding="utf8").read() + open("Most-populars-words.txt",encoding="utf8").read()
books_word = word_tokenize(books)

word_tags = (nltk.pos_tag((books_word), tagset="universal"))

noun_dict = []
verb_dict = []
adjective_dict = [] 

@eel.expose
def Word_Noun():
    global word_noun
    for x in word_tags:
        if x[1] == "NOUN":
            noun_dict.append(x[0])
    
    noun_dict_range = len(noun_dict)
    noun_id = randint(0,noun_dict_range)
    word_noun = noun_dict[noun_id]

@eel.expose
def Word_Verb():
    global word_verb
    for x in word_tags:
        if x[1] == "VERB":
            verb_dict.append(x[0])
    
    verb_dict_range = len(verb_dict)
    verb_id = randint(0,verb_dict_range)
    word_verb = verb_dict[verb_id]

@eel.expose
def Word_Adjective():
    global word_adjective
    for x in word_tags:
        if x[1] == "ADJ":
            adjective_dict.append(x[0])
    
    adjective_dict_range = len(adjective_dict)
    adjective_id = randint(0,adjective_dict_range)
    word_adjective = adjective_dict[adjective_id]

@eel.expose
def first_group():
    Word_Verb()
    answer = word_verb + "!"
    return answer

@eel.expose
def second_group():
    Word_Verb()
    Word_Noun()
    Word_Adjective()


    answer = word_verb +" " + word_noun
    answer2 = word_verb + " " + word_adjective

    x = randint(0,1)
    if x == 0:
        return answer
    elif x == 1:
         return answer2

@eel.expose
def third_group():
    Word_Noun()
    Word_Adjective()
    answer = word_noun + " is " + word_adjective
    return answer

@eel.expose
def fourth_group(name):
    Word_Adjective()

    answer = name + " is " + word_adjective
    return answer

@eel.expose
def help():
    answer = '''Lai izveidotu saukli, noklikšķiniet uz vienas no pogām:
    1. Noklikšķinot uz pogas "1.grupa", tiks ģenerēts sauklis ar struktūru "Darbības vārds".
    2. Noklikšķinot uz pogas "2.grupa", tiks ģenerēts sauklis ar struktūru "Darbības vārds + lietvārds vai darbības vārds + īpašības vārds".
    3. Noklikšķinot uz pogas "3.grupa", tiks ģenerēts sauklis ar struktūru "Lietvārds + darbības vārds “is” + īpašības vārds".
    4. Noklikšķinot uz pogas "4.grupa", tiks ģenerēts sauklis ar struktūru "Uzņēmuma nosaukums (vai vārds) + darbības vārds “is” + īpašības vārds". Lai uzrakstītu uzņēmuma nosaukumu, ievadiet to tekstlodziņā.'''
    return answer

@eel.expose
def informacija():
    answer = ''' Kā datu bāzi saukļu ģenerēšanai programma izmanto grāmatas “100 ways to motivate others pt1”, “100 Ways to Motivate Yourself Change Your Life Forever” un sarakstu ar 1000 vispopulārākajiem angļu valodā vārdiem.
Saukļi ir sadalīti 4 grupās, kas atšķiras pēc gramatiskās struktūras un garuma. 
Saukļi no 1.grupas sastāv tikai no  darbības vārda, piemēram, sauklis “Think” (IBM).
Saukļi no 2.grupas sastāv  no  darbības vārda un lietvārda vai no darbības vārda un īpašības vārda, piemēram,  sauklis “Think different” (Apple).
Saukļi no 3.grupas sastāv  no  lietvārda, darbības vārda “is” un īpašības vārda, piemēram, sauklis “Life is good” (Sony).
Saukļi no 4.grupas sastāv no  uzņēmuma nosaukuma darbības vārda “is” un īpašības vārda , piemēram,  sauklis “DK.Corp is uniqueness”.
Programmas autors: Austrumlatvijas Tehnoloģiju vidusskolas 11.B klases skolnieks Daniils Krasnovs'''
    return answer

@eel.expose
def clear():
    answer = ''
    return answer




eel.init("")
eel.start("main.html",size=(700,500))