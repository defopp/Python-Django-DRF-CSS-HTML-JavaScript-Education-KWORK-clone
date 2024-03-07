from django.urls import path

from productsApp.views import MainCategoryView, SubCategoryView, CatalogView, new_project

urlpatterns = [
    path('', CatalogView.as_view(), name='catalogURL'),
    path('<str:mainurlname>', MainCategoryView.as_view(), name='maincategoryURL'),
    path('<str:mainurlname>/<str:suburlname>', SubCategoryView.as_view(), name='subcategoryURL'),
    
    path('new_project/', new_project.as_view(), name='new_project'),
    # path('project/<int:id>')
]
