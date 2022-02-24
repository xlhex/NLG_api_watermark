#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli
#Version  : 1.0
from __future__ import print_function

import sys

import spacy
from collections import defaultdict
from tqdm import tqdm

from nltk.corpus import wordnet


def main(orig_file, candidate_path, watermark_idx_file):
    word_pos = "ADJ"

    most_common = defaultdict(lambda: defaultdict(list))
    id2word = {}
    counter = 0
    # load candidate words
    with open(candidate_path) as reader:
        for line in reader:
            words = line.strip().split()
            key = words[0]
            most_common[words[0]][word_pos].extend(words)
            id2word[counter] = key
            counter += 1
    
    target_words = set(most_common.keys())
    num_target_words = len(target_words)

    nlp = spacy.load("en_core_web_lg")

    sents = []

    with open(orig_file) as reader:
        for line in reader:
            sents.append(line.strip())

    secret_keys = {}

    # load watermarked indices
    with open(watermark_idx_file) as reader:
        for i, line in enumerate(reader):
            secret_keys[id2word[i]] = int(line)

    # watermark target words
    for i, sent in enumerate(tqdm(sents)):
        if len(target_words - set(sent.split())) < num_target_words:
            words = []
            doc = nlp(sent.strip())
            for token in doc:
                if token.text in most_common:
                    if token.pos_ in most_common[token.text]:
                        cands = most_common[token.text][token.pos_]
                        words.append(cands[secret_keys[token.text]])
                    else:
                        words.append(token.text)
                else:
                    words.append(token.text)
            print(" ".join(words))
        else:
            print(sent)

if __name__ == "__main__":
    main(*sys.argv[1:])
