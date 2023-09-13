#!/usr/bin/python3

def best_score(a_dictionary):
    max_key = max(a_dictionary, key=a_dictionary.get)
    max_value = a_dictionary[max_key]
    return max_value