# PTOS (PlaceToSpeak) 0.1
Django 
## Setup
`pip install -r requirements.txt`

Rename and edit `CONFIG_EXAMPLE.py` > `CONFIG.py`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py collectstatic`

`python ./private/create_user_tree.py`

`python ./load_to_db.py`
## Start app
`python manage.py runserver 127.0.0.1:80`
