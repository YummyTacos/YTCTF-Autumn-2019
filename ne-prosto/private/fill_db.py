#!/usr/bin/env python3
from binascii import unhexlify, hexlify
from sys import argv

from Crypto.PublicKey import RSA


def data(n):
    return unhexlify(f'{n:0128x}')


if len(argv) < 2:
    print(f'Usage: {argv[0]} [db_filename]')
    exit(1)

try:
    with open(argv[1], 'rb') as f:
        r = f.read()
except FileNotFoundError:
    open(argv[1], 'w')
    r = ''

if len(r) % 64:
    print('Length must be a multiple of 64')
    exit(1)

s = set(int(hexlify(r[i:i + 64]), 16) for i in range(0, len(r), 64))
while True:
    key = RSA.generate(2 ** 10)
    if key.p not in s:
        with open(argv[1], 'ab') as f:
            f.write(data(key.p))
        s.add(key.p)
    if key.q not in s:
        with open(argv[1], 'ab') as f:
            f.write(data(key.q))
        s.add(key.q)
    print(len(s))
