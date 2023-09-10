#!/usr/bin/python3

def uniq_add(my_list=[]):
    number = 0
    for num in set(my_list):
        number += num
    return number
