#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "Jordan Davidson"

import sys


def find_anagrams(words):
    anagrams = {}
    for word in words:
        if ''.join(sorted(word)) not in anagrams:
            anagrams[''.join(sorted(word))] = [word]
        else:
            anagrams[''.join(sorted(word))] += [word]
    return anagrams


if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print(ind_anagrams(words))
