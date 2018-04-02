#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Galvanize Data Scientist application:
# https://app.formassembly.com/418492?contactID=0030a00001uKYRI&tfa_14=a0K0a00000hWuNa

# Repo: https://github.com/avibrazil/Galvanize-Data-Science-Acceptance


from collections import defaultdict, OrderedDict
import sys, re
from operator import itemgetter

sentences = 0
lines = 0 
word = 0


print 'Text analysis from standard input or from file name passed as first argument:'
print '$ cat text.txt | ./q1.py'
print '$ ./q1.py text.txt\n'

if len(sys.argv) > 1:
    f = open(sys.argv[1]).read()
else:
    f = sys.stdin.read()


d = defaultdict(int)
for word in f.split():
    d[word] += 1
distinct_word = d.items()

sentences = [s.strip() for s in re.split('[\.\?!]', f) if s]
lines = f.split('\n')


print '★ Total word count =>', len(f.split())
print '★ Unique word count =>',len(distinct_word)
print '★ Number of sentences =>', len(sentences)
print '★ Number of lines =>', len(lines)
print '★ Average word count in sentence =>', float(len(f.split())/len(sentences))


W = re.findall(r"[\w']+", f)
#print 'Words=', '\n', W, '\n'


def phrases(w):
        phrase = []
        for w in W:
            p = phrase.append(w)
            if len(phrase) > 3:
                phrase.remove(phrase[0])
            if len(phrase) == 3:
                yield tuple(phrase)

#print 'list of phrases',list(phrases(W)), '\n'

Phrases = defaultdict(int)
for p in phrases(W):
        Phrases[p] += 1

sorted_phrases=sorted(Phrases.items(), key=itemgetter(1), reverse = True)

# print '★ Sorted Phrases By Count: ', '\n', sorted_phrases, '\n'

print '\n★ Frequent Phrases (more than 3 times): '
for k, (phrase, freq) in enumerate(sorted_phrases):
    if freq > 2:
        print phrase, freq, '\n',
    else:
        break

s = sorted(d.items(), key=itemgetter(1), reverse =True)
print "\n★ List of Words in Descending Count:",'\n'
for k, (words, count) in enumerate(s):
    print words, count
