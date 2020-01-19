#!/usr/bin/env python3
from binascii import unhexlify
from re import findall
from socket import create_connection
from sys import argv


def gcd(a, b):
    if b:
        d, x, y = gcd(b, a % b)
        return d, y, x - y * (a // b)
    return a, 1, 0


def decode(n, p, c, e=65537):
    q = n // p
    if n != p * q:
        return
    phi = (p - 1) * (q - 1)
    d = gcd(e, phi)[1]
    if d < 0:
        d += phi
    m = f'{pow(c, d, n):x}'
    if len(m) % 2:
        m = '0' + m
    print(unhexlify(m).decode())
    input()


def check(keys, added):
    for i in keys:
        a = gcd(i, added)[0]
        if a != 1 and i != added:
            print(i, a, keys[i])
            decode(i, a, keys[i])


def get_key(host, port):
    s = create_connection((host, port))
    m = s.recv(1024).decode()
    while 'c: ' not in m:
        m += s.recv(1024).decode()
    s.close()
    return findall('n: (\\d+)\ne: \\d+\nc: (\\d+)', m)[0]


def main():
    if len(argv) < 3:
        print(f'Usage: {argv[0]} [host] [port]')
        exit(1)

    keys = {}

    while True:
        n, c = map(int, get_key(argv[1], argv[2]))

        check(keys, n)

        keys[n] = c
        print(len(keys))


if __name__ == '__main__':
    main()
