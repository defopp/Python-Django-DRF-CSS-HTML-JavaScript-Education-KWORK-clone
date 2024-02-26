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




available urls
    urlpatterns = [
        # main pages
        path('admin/', admin.site.urls),
        path('', MainPage, name='main'),
        path('to_freelancer/', ToFreelancerPage, name='freelancer'),
        path('create_project/', ProjectCreatePage),
        
        
        # pages moded with api
        path('category/', CategoryPage),
        path('category/catalog/', CategoryCatalogPage),
        path('project/', ProjectPage),
        path('user_profile/', UserProfilePage),
        path('messenger/', MessengerPage),
    ]