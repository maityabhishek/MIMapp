# Python program to demonstrate
# command line arguments


from nltk.tokenize import word_tokenize
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

count = 2
if n == count:
    print('1234')

agenda = 'Caliber sync up'


agendaWordList = word_tokenize(agenda)
print(agendaWordList)
