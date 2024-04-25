runproject flow
    create venv    
        py -m venv .\venv
    activate venv
        .\venv\Scripts\activate
    install req
        pip install -r requirements.txt
    
    run server
        cd .\DjangoProject\
        py manage.py runserver




available urls:
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







usersApp
    signupView - GET(Страница регистрации) POST(Форма регистрации)
    loginView - GET(Страница авторизации) POST(Форма авторизации)
    logoutView - GET(Выход из аккаунта)
    profileView - GET(Страница пользователя по ID)
    myProfileView - GET(Страница аккаунта пользователя запроса)
    editProfileView - GET(Страници редактирования аккаунта) POST(Форма смены пароля)

productsApp
    CatalogBuyView - GET(Страница каталога категорий)
    CatalogSellView - GET(Страница каталога проектов на продажу)
    MainCategoryView - GET(Страница главной категории)
    SubCategoryView - GET(Страница подкатегории)
    new_projectView - GET(Страница создания проекта) POST(Форма создания проекта)
    ProjectView - GET(Страница просмотра проекта)