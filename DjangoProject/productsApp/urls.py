from django.urls import path

from productsApp.views import MainCategoryView, SubCategoryView, CatalogView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalogURL'),
    path('<str:mainurlname>', MainCategoryView.as_view(), name='maincategoryURL'),
    path('<str:mainurlname>/<str:suburlname>', SubCategoryView.as_view(), name='subcategoryURL')
]
