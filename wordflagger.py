
"""
Python program to parse key words from Theme Camp interactivity descriptions.
Original code came from Google python exercise on wordcount -- thanks Google!

"""

import sys

#
def print_words(filename) :
# create a tuple with key = (lower case word) and value = (incrementing count)
#   will either iterate throught the list or perhaps a while loop
# Once tuple created, sort by value desc and print
  word_count = {}
  f = open(filename, 'r')
  for line in f: 
    words = line.split()
    for word in words:
      word = word.lower()
      if not word in word_count : word_count[word] = 1
      else :
        word_count[word] += 1
  f.close() 
# this last step added to give sort in order of most freq to least
  vsort = sorted(word_count.items(), key= lambda t : t[1], reverse=True)
  for elem in vsort : print elem #added print to return vertical list in freq order
  return 


###
def print_top(filename,freq) :
  word_count = {}
  f = open(filename, 'r')
  for line in f: 
    words = line.split()
    for word in words:
      word = word.lower()
      if not word in word_count : word_count[word] = 1
      else :
        word_count[word] += 1
  f.close() 
# Added list of words to flag/print if seen
  flaglist = ['fire','flame','adult','sex','pornography','food','kitchen',
              'yoga','chill','friends','namiste','artcar','children','kids',
              'minors','enema']
  supresslist = ['and','we','the','burning','man','playa','to','of','our',
                  'that','will','have','a','be','us','you','know','are']
# this last step added to give sort in order of most freq to least
# created freq filter so any keyword with more than 3 occurances is returned
#   --> Perhaps make the freq a configurable parameter read in at begining.
  vsort = sorted(word_count.items(), key= lambda t : t[1], reverse=True)
  for elem in vsort :
    if elem[0] not in supresslist and elem[1] >= freq : print elem
    elif elem[0] in flaglist : print elem 
  return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 4:
    print 'usage: ./wordcount.py {--count | --topcount} file min_freq'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    freq = sys.argv[3]  
    print_top(filename,freq)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
