#!/usr/bin/python3
def remove_char_at(str, n):
    s2 = ''
    for s, j in enumerate(str):
        if s == n:
            continue
        s2 += j
    return(s2)
