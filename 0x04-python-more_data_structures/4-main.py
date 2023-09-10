#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_element').only_diff_element

set_1 = { "Python", "C", "JavaAscript" }
set_2 = { "Bash", "C", "Ruby", "Pear" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
