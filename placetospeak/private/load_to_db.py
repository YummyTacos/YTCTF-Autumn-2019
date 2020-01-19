import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ptos.settings')
django.setup()


if __name__ == '__main__':
    import json
    from random import randint, choice
    from feed.models import Post, Friend
    from django.contrib.auth.models import User

    Post.objects.all().delete()
    Friend.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()

    with open('private/friends.json') as f_f:
        friends = json.load(f_f)
        user = [None]*100

        print('Make admins and theirs posts')
        with open('private/admin_posts.json') as f:
            admin_posts = json.load(f)
            for p in admin_posts:
                if not User.objects.filter(username=p['author']).exists():
                    User.objects.create_user(username=p['author'], password='0')
                    # Put user in list
                    for i in friends['ends'][::-1]:
                        if user[i] is None:
                            user[i] = p['author']
                            break
                post = Post()
                post.author = User.objects.get(username=p['author'])
                post.text = p['text']
                if 'isPublic' in p:
                    post.isPublic = p['isPublic']
                post.save()

        print('Make random users and their random posts')
        with open('private/random_users.json') as f_u, open('private/random_posts.json', encoding='utf-8') as f_posts, \
                open('private/passwords.json') as f_pass:
            users = json.load(f_u)
            posts = json.load(f_posts)
            passwords = json.load(f_pass)
            for u in users:
                # Put user in list and setup password
                for i in range(100):
                    if user[i] is None:
                        user[i] = u
                        if i in friends['ends']:
                            User.objects.create_user(username=u, password='0')
                        else:
                            User.objects.create_user(username=u, password=choice(passwords))
                        break
                # Put random posts
                col = randint(2, 8)
                for i in range(col):
                    p = posts.pop(randint(0, len(posts)-1))
                    post = Post()
                    post.author = User.objects.get(username=u)
                    post.text = p
                    post.save()

        print('Make friends')
        for a, b in friends['friends']:
            friend = Friend(
                creator=User.objects.get(username=user[a]),
                following=User.objects.get(username=user[b])
            )
            friend.save()

        print('Public users')
        for i in range(5):
            if Friend.objects.filter(following=User.objects.get(username=user[i])).exists():
                break
            else:
                post = Post.objects.filter(author=User.objects.get(username=user[i]))[0]
                print(post)
                setattr(post, 'isPublic', True)
                post.save()
