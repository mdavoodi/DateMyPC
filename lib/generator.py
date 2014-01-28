import PhraseGenerator, nltk
from random import randint
gen = PhraseGenerator.PhraseGenerator(nltk.corpus.brown, 'dirty.txt')

f = open('./sources/dirty.txt', 'r')
start = []
for line in f:
    start.append(line.split(' ')[0])


def generate():
    return gen(start[randint(0,len(start)-1)])

