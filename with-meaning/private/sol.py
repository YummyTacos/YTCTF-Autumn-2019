#!/usr/bin/env python3
with open('cipher', 'r') as f:
    r = (map(int, i.split('.')) for i in f.read().split('  '))

with open('Message.txt', 'r') as f:
    text = f.read().split('\n')

for i, j in r:
    print(text[i][j], end='')
