from heapq import nlargest
import urllib.request
import bs4 as BeautifulSoap
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = urllib.request.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
article = text.read()
# print(article)

article_parsed = BeautifulSoap.BeautifulSoup(article, 'html.parser')
paragraphs = article_parsed.find_all('p')
article_content = ''
for p in paragraphs:
    article_content += p.text
# print(article_content)
stop_words = stopwords.words('english')
punctuation = punctuation + '\n'
# print(punctuation)

tokens = word_tokenize(article_content)

word_frequencies = {}
for word in tokens:
    if word.lower() not in stop_words:
        if word.lower() not in punctuation:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
# print(word_feequencies)

max_frequency = max(word_frequencies.values())
# print(max_frequency)
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

sentences = sent_tokenize(article_content)
sentence_weight = dict()
for sentence in sentences:
    sentence_wordcount = (len(word_tokenize(sentence)))
    sentence_wordcount_without_stop_words = 0
    for word_weight in word_frequencies:
        if word_weight in sentence.lower():
            sentence_wordcount_without_stop_words += 1
            if sentence in sentence_weight:
                sentence_weight[sentence] += word_frequencies[word_weight]
            else:
                sentence_weight[sentence] = word_frequencies[word_weight]
    sentence_weight[sentence] = sentence_weight[sentence]
# print(sentence_weight)

select_length = int(len(sentence_weight)*0.3)
summary = nlargest(select_length, sentence_weight, key=sentence_weight.get)

final_summary = [word for word in summary]
summary = ''.join(final_summary)
# print(summary)
print(len(article_content))
print(len(summary))
