from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk
from nltk.corpus import wordnet

def set_agenda_meeting(agenda_proposed):
    global agenda 
    agenda = agenda_proposed
    
def set_meeting_context():
    nouns = []
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(agenda))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)
    print(nouns)   
    array_synonyms=[]
    for noun_word in nouns:
        for vsyn in wordnet.synsets(noun_word):
            #print(vayn)
            for l in vsyn.lemmas():
                array_synonyms.append(l.name())
    print(set(array_synonyms))
set_agenda_meeting("Prince Philip has died aged 99, Buckingham Palace announces")
set_meeting_context()
    
def cosine_similarity_with_agenda(sentence):
    agenda_list = word_tokenize(agenda) 
    sentence_list = word_tokenize(sentence)

    # sw contains the list of stopwords
    sw = stopwords.words('english') 
    l1 =[];l2 =[]

    # remove stop words from the string
    agenda_set = {w for w in agenda_list if not w in sw} 
    sentence_set = {w for w in sentence_list if not w in sw}

    # form a set containing keywords of both strings 
    rvector = agenda_set.union(sentence_set) 
    for w in rvector:
        if w in agenda_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in sentence_set: l2.append(1)
        else: l2.append(0)
    c = 0

    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    #we can use this similarity % to add extra weightage to our prog 
    
    print("similarity: ", cosine)
#set_agenda_meeting("talking points regarding the hackathon azure")    
#cosine_similarity_with_agenda("azure is great to talk about")
set_meeting_context()
