#!/usr/bin/python3
common_elements = __import__('3-common_element').common_element

set_1 = { "Python", "C", "JavaAscript" }
set_2 = { "Bash", "C", "Ruby", "Pear" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
