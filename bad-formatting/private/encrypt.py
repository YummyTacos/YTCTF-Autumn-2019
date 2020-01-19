from sys import argv
from random import randint

if len(argv) < 4:
    print(f'{argv[0]} container code.ws comments output_file')
    exit(-1)

with open(argv[1], 'r') as f:
    c_code = f.read()

while '  ' in c_code:
    c_code = c_code.replace('  ', ' ')
c_code = c_code.split('\n')

with open(argv[2], 'r') as f:
    ws_code = f.read().split('\n')

with open(argv[3], 'r') as f:
    comments = f.read().split('\n')

for comment in comments:
    pos = randint(20, len(c_code))
    c_code = c_code[:pos] + [comment] + c_code[pos:]

while len(c_code) != len(ws_code):
    c_code.append('')

bad_words = ['static', 'int', 'char', 'const', 'return', 'void', 'typedef', 'struct', 'treap', 'treap_t', 'else']
for i in range(len(ws_code)):
    used = 0
    line = c_code[i].split(' ')

    needed = 0
    for j in range(len(line)):
        if line[j] in bad_words:
            needed += 1
    if needed > len(ws_code[i]):
        c_code = c_code[:i] + [''] + c_code[i:]

    line = c_code[i].split(' ')
    for j in range(len(line) - 1):
        if line[j] in bad_words:
            needed -= 1
            rng = 1
        else:
            rng = randint(0, len(ws_code[i]) - used - needed)
        line[j] += ws_code[i][used:used + rng]
        used += rng
    line[-1] += ws_code[i][used:]
    c_code[i] = ''.join(line)

with open(argv[4], 'w') as f:
    f.write('\n'.join(c_code))
