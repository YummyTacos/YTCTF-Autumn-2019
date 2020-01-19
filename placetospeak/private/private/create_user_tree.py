from random import choice
import json

friends, ends, layers = [], [], 0


def create_tree():
    global friends, ends, layers
    col = choice([2, 3])
    tops = list(range(col))
    user = col
    layers = 1

    while True:
        new_tops = []
        for top in tops:
            col = choice([0, 0, 2, 3])
            if col == 0:
                ends.append(top)
            else:
                if user + col <= 100:
                    new_tops += list(range(user, user + col))
                    friends += [(top, i) for i in range(user, user + col)]
                    user = user + col
                else:
                    new_tops += list(range(user, 100))
                    friends += [(top, i) for i in range(user, 100)]
                    user = 100
        tops = list(new_tops)
        layers += 1
        if user >= 100:
            ends += tops
            break


if __name__ == '__main__':
    create_tree()
    print(friends)
    print(ends)
    print(layers)

    name = input('Enter name of file to save: (recommended: friends.json)')
    if name != '':
        with open(name, 'w') as f:
            json.dump({'friends': friends, 'ends': ends}, f)
            exit('Success!')
        exit('Error writing')
    exit('Not saved')
