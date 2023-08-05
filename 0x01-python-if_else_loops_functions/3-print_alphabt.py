#!/usr/bin/python3
for aph in range(97, 123):
    if aph == 101 or aph == 113:
        continue
    print('{}'.format(chr(aph)), end='')
