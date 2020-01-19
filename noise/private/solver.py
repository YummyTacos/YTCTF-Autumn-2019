from PIL import Image

FILE = 'pic.png'


def solve():
    im = Image.open(FILE)
    data = list(im.getdata())
    alp = {}
    ch = 'a'
    for i in data:
        if i != (0,) * 3:
            if i not in alp:
                alp[i] = ch
                ch = chr(ord(ch) + 1)
            print(alp[i], end='')


if __name__ == '__main__':
    solve()
