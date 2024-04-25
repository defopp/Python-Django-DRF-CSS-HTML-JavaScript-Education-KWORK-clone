from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from productsApp.views import MainCategoryView, SubCategoryView, CatalogBuyView, CatalogSellView, new_projectView, ProjectView

urlpatterns = [
    path('id/<int:project_id>', ProjectView.as_view(), name='project'),
    path('new_project/', new_projectView.as_view(), name='new_project'),
    
    path('', CatalogBuyView.as_view(), name='catalogBuyURL'),
    path('sell', CatalogSellView.as_view(), name='catalogSellURL'),
    path('<str:mainurlname>', MainCategoryView.as_view(), name='maincategoryURL'),
    path('<str:mainurlname>/<str:suburlname>', SubCategoryView.as_view(), name='subcategoryURL'),
]
