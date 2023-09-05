#!/usr/bin/python3

def multiple_returns(sentence):
    
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple =0, None

    my_tuple = len(sentence), sentence[0]
    return my_tuple
