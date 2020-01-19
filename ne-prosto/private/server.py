#!/usr/bin/env python3
from binascii import hexlify
from random import randint
from sys import argv
from time import sleep
from os import stat

from Crypto.PublicKey import RSA

FLAG = 'ytctf{SmOOl_DB_iS_v3Ry_B4d}'

if len(argv) < 2:
    print(f'Usage: {argv[0]} [db_filename]')
    exit(1)

m = int(hexlify(FLAG.encode()), 16)
e = 65537

try:
    f = open(argv[1], 'rb')
except FileNotFoundError:
    print('File not found')
    exit(1)

size = stat(argv[1]).st_size
if size % 64:
    print('Length must be a multiple of 64')
    exit(1)
size //= 64

print('Encrypting flag for you', end='')
for i in range(5):
    print('.', end='')
    sleep(1)

p, q = randint(0, size - 1), randint(0, size - 1)
while p == q:
    q = randint(0, size - 1)
if p > q:
    p, q = q, p

f.seek(p * 64)
t = int(hexlify(f.read(64)), 16)
f.seek((q - p - 1) * 64)
q = int(hexlify(f.read(64)), 16)
p = t

try:
    key = RSA.construct((p * q, e))
except ValueError:
    print('Bad data')
    exit(1)

print('\nReady!')
sleep(1)
print(f'n: {p * q}\ne: {e}\nc: {pow(m, e, p * q)}')
