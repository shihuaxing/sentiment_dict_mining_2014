__author__ = 'egor'

"""
Script parameters:
    1: name of file with positive words, which were found by our algorithms (will be tested)
    2: name of file with negative words, which were found by our algorithms
    3: name of file with neutral words, which were found by our algorithms
    4: filename of 500-dictionary positive words (for completeness test)
    5: filename of 500-dictionary negative words (for completeness test)
    6: Big dictionary positive words filename
    7: Big dictionary negative words filename
    8: Big dictionary neutral words filename

While execution, you'll need to mark new for big dictionary words from console

Script will create three files in a working directory with names:
    'big_ext_pos.txt',    - new marked positive words
    'big_ext_neg.txt',    - new marked negative words
    'big_ext_neutral.txt' - new marked neutral words
"""

import sys


def read_pos(dict_to_add, filename):
    f = open(filename, 'r')
    for s in f:
        if s.strip(' \n') not in dict_to_add:
            dict_to_add[s.strip(' \n')] = 1
    f.close()


def read_neg(dict_to_add, filename):
    f = open(filename, 'r')
    for s in f:
        if s.strip(' \n') not in dict_to_add:
            dict_to_add[s.strip(' \n')] = -1
    f.close()


def read_neutral(dict_to_add, filename):
    f = open(filename, 'r')
    for s in f:
        if s.strip(' \n') not in dict_to_add:
            dict_to_add[s.strip(' \n')] = 0
    f.close()


if len(sys.argv) < 9:
    sys.exit("Bad arguments!")

completeness_dict = {}  # given completeness 500-dict
big_dict = {}           # given big dictionary
big_ext_dict = {}       # new words to add
new_dict = {}           # dictionary, which were found by our algorithm

#reading dictionaries
read_pos(new_dict, sys.argv[1])
read_neg(new_dict, sys.argv[2])
read_neutral(new_dict, sys.argv[3])
read_pos(completeness_dict, sys.argv[4])
read_neg(completeness_dict, sys.argv[5])
read_pos(big_dict, sys.argv[6])
read_neg(big_dict, sys.argv[7])
read_neutral(big_dict, sys.argv[8])

completeness_value = 0  # number of guessed words from 500-dictionary
quality_value = 0       # number of guessed words from big dictionary

# iterating through words from generated by algorithms dictionary and counting guessed words.
for key in new_dict.keys():
    if key in completeness_dict and completeness_dict[key] == new_dict[key]:
        completeness_value += 1
        quality_value += 1 # if word in 500-dict => it's in big dict too
    elif key in big_dict and big_dict[key] == new_dict[key]:
        quality_value += 1
    elif key not in big_dict and key not in big_ext_dict:  # means, that we found a new word
        p = 2
        while p not in [1, -1, 0]:
            print('Mark new word (1, -1 or 0) ' + key + ': ')
            p = int(sys.stdin.readline())
        big_ext_dict[key] = p

print('Completeness value: ' + str(completeness_value) + ' => '
      + str(completeness_value * 100 / len(completeness_dict)) + '%')

print('Quality value: ' + str(quality_value) + ' => '
      + str(quality_value * 100 / len(big_dict)) + '%')

f_pos = open('big_ext_pos.txt', 'w')
f_neg = open('big_ext_neg.txt', 'w')
f_neutral = open('big_ext_neutral.txt', 'w')

for key in big_ext_dict:
    if big_ext_dict[key] == 0:
        f_neutral.write(key + '\n')
    if big_ext_dict[key] == -1:
        f_neg.write(key + '\n')
    if big_ext_dict[key] == 1:
        f_pos.write(key + '\n')

f_pos.close()
f_neg.close()
f_neutral.close()