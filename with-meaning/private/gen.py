#!/usr/bin/env python3
from re import finditer
from random import choice

flag = 'ytctf{uuuh_icansee_that_this_text_issosmisloy_good_job_m8}'
s_flag = set(i for i in flag)

with open('Message.txt', 'r') as f:
    text = f.read().split('\n')

d = dict([(i, set()) for i in s_flag])

for index, line in enumerate(text):
    if line:
        for i in flag:
            d[i].update(set([f'{index}.{pos.start()}' for pos in finditer(i, line)]))

with open('cipher', 'w') as f:
    for i in flag:
        f.write(f'{choice(list(d[i]))}  ')
