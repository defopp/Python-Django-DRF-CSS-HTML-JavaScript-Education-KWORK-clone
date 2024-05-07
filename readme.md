# Копия биржи фриланса KWORK
- [Дизайн в Figma.com](https://www.figma.com/file/RPZaZR9gVgVTuSrD9GnmAE/%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%91%D0%B8%D1%80%D0%B6%D0%B8-%D0%A4%D1%80%D0%B8%D0%BB%D0%B0%D0%BD%D1%81%D0%B0?type=design&t=ZxV5FBVWbCz9x8aX-6)

### Тестовый запуск:
###### 1. create/activate venv    
    py -m venv .\venv
    .\venv\Scripts\activate
###### 2. install requirements
    pip install -r requirements.txt
###### 3. run server
    cd .\DjangoProject\
    py manage.py runserver




### Available urls:
    / [name='main']
    to_freelancer/ [name='freelancer']
    users/
        signup/ [name='signup']
        login/ [name='login']
        logout/ [name='logout']
        <int:pk> [name='profile']
        myprofile/ [name='myprofile']
        myprofile/settings/ [name='user_settings']
    projects/ [name'catalogURL']
        id/<int:project_id> [name'project']
        new_project/ [name'new_project']
        <str:mainurlname> [name'maincategoryURL']
        <str:mainurlname>/<str:suburlname> [name'subcategoryURL']
    messages/