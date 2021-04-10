import nltk

from nltk.corpus import wordnet

array_synonyms=[]
array_antonyms=[]


#print(wordnet.synsets("good"))
#print(wordnet.synonyms("good"))
for vsyn in wordnet.synsets("good"):
    #print(vayn)
    for l in vsyn.lemmas():
        #print(l.name());
        array_synonyms.append(l.name())
        if l.antonyms():
            #print(l.antonyms())
            array_antonyms.append(l.antonyms()[0].name())

print(set(array_synonyms))
print(set(array_antonyms))
