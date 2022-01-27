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
    answer = '''Lai izveidotu saukļu, noklikšķiniet uz vienas no pogām
    1. Noklikšķinot uz pogas "1.grupa", tiks ģenerēts saukļus pēc veidnes: "Darbības vārds"
    2. Noklikšķinot uz pogas "2.grupa", tiks ģenerēts saukļis pēc veidnes: "Darbības vārds + lietvārds vai darbības vārds + īpašības vārds"
    3. Noklikšķinot uz pogas "3.grupa", tiks ģenerēts saukļus pēc veidnes: "Lietvārds + darbības vārds “is” + īpašības vārds"
    4. Noklikšķinot uz pogas "4.grupa", tiks ģenerēts saukļus pēc veidnes: "Uzņēmuma nosaukums (vai vārds) + darbības vārds “is” + īpašības vārds", lai uzrakstītu uzņēmuma nosaukumu, ievadiet to tekstlodziņā'''
    return answer

@eel.expose
def informacija():
    answer = ''' Lai noskaidrotu biežāk lietotos šablonus, tika analizēti aptuveni 150 dažādi populāri reklāmas saukļi angļu valodā dažādās jomās un
     izplatītākās teikumu struktūras tika sadalītas 3 grupās un apkopotas tabulā.
     Informācija tika sagrupēta 3 grupās, kas atšķiras pēc teikuma uzbūves un saukļa garuma.Šajās trīs pamata struktūrās saukļu veidošanā neparādās uzņēmuma nosaukums, tomēr dažreiz uzņēmumi vēlētos iekļaut savus nosaukumus vai izvēlētus vārdus.
     Tāpēc autors nāca klajā ar papildus struktūru. Par pamatu tika ņemta 3. grupa
    '''
    return answer

@eel.expose
def clear():
    answer = ''
    return answer











eel.init("web")
eel.start("main.html",size=(700,500))