#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli
#Version  : 1.0
from __future__ import print_function

import numpy as np
import math
import sys
from scipy.stats import binom


def main(sub_idx_file, sub_file, eval_file):

    trial = []
    hits = []
    n_trials = 0
    n_hits = 0
    hash_map = []

    # load watermarked indices
    with open(sub_idx_file) as f:
        for line in f:
            hash_map.append(int(line))

    # load candidates and their synonyms
    with open(sub_file) as f:
        for i, line in enumerate(f):
            words = line.strip().split()
            if i == 0:
                p = 1 / len(words)
            trial.extend(words)
            hits.append(words[hash_map[i]])

    # count hits
    with open(eval_file) as reader:
        for line in reader:
            for word in line.strip().split():
                if word in trial:
                    n_trials += 1
                if word in hits:
                    n_hits += 1

    print(n_hits, n_trials, p)
    right_results = 0
    for i in range(n_hits, n_trials+1):
        right_results += binom.pmf(i, n_trials, p)
    left_results = 0
    for i in range(n_hits):
        left_results += binom.pmf(i, n_trials, p)
    print(right_results, left_results)
    print(2*min(right_results, left_results))


if __name__ == "__main__":
    main(*sys.argv[1:])

