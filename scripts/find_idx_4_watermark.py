#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli
#Version  : 1.0
from __future__ import print_function

import numpy as np
import sys
from scipy.stats import binom


def main(sample_file, syns_file, topK):

    trial = []
    hits = []
    n_trials = 0
    n_hits = 0

    topK = int(topK)

    with open(syns_file) as f:
        for i, line in enumerate(f):
            if i >= topK: break
            words = line.strip().split()
            if i == 0:
                p = 1 / len(words)
            trial.extend(words)
            idx = hash(line.strip()) % len(words)
            print(idx)
            hits.append(words[idx])

    with open(sample_file) as reader:
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

