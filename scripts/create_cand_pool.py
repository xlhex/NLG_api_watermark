#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli
#Version  : 1.0
from __future__ import print_function

import sys


def main(orginal_file, num_cand):
    src_words, type_list, cands_list = [], [], []
    src_set = set()
    cands_set = set()
    # read candidates and their synonyms
    with open(orginal_file) as f:
        for line in f:
            src_word, type, cands = line.strip().split("\t")
            cands = cands.split()
            src_words.append(src_word)
            src_set.add(src_word)
            type_list.append(type)
            cands_list.append(cands)
            cands_set.update(set(cands))

    used = set()
    valid_set = cands_set - src_set

    K = int(num_cand)
    
    # create lookup for substitution
    for i in range(len(src_words)):
        src_word = src_words[i]
        cands = cands_list[i]
        # remove selected words
        valid_cands = set(cands) & valid_set - used
        # selec candiates having more than K synonyms
        if len(valid_cands) >= K:
            selected_sysns = []
            count = 0
            for cand in cands:
                if cand in valid_set and cand not in used:
                    used.add(cand)
                    selected_sysns.append(cand)
                    count += 1
                if count >= K:
                    break
            print(" ".join([src_word] + selected_sysns))


if __name__ == "__main__":
    main(*sys.argv[1:])

