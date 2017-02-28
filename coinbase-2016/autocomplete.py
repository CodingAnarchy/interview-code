import re

def dmerge(a, b):
    for k, v in b.items():
            if isinstance(v, dict) and k in a:
                dmerge(a[k], v)
            else:
                a[k] = v

def find_shortest(tree):
    max_len = 99999999
    current_path = []
    for k, v in tree.items():
        if not isinstance(v, dict):
            return [k, v]
        else:
            new_path = find_shortest(v)
            if len(new_path) < max_len:
                current_path = [k] + new_path

    return current_path

word_list = ['apple', 'banana', 'pear', 'app']
word_dict = {}


for word in word_list:
    word_d = dict()
    for idx, ch in enumerate(reversed(word)):
        if idx == 0:
            val = ch
        elif idx == 1:
            word_d = {ch: val}
        elif idx < len(word) - 1:
            word_d = {ch: word_d}
        else:
            if ch not in word_dict:
                word_dict[ch] = word_d
            else:
                dmerge(word_dict[ch], word_d)


while True:
    inp = raw_input('Prefix: ')

    not_found = False
    d = word_dict
    complete = []
    for ch in inp:
        if ch not in d:
            not_found = True
        else:
            if isinstance(d, str):
                not_found = True
            else:
                 d = d[ch]
                 complete += [ch]

    if not_found:
        print inp
    else:
        if isinstance(d, str):
            print inp + d
        else:
            complete += find_shortest(d)
            print ''.join(complete)
