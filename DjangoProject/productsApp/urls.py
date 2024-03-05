from django.urls import path

from productsApp.views import MainCategoryView, SubCategoryView

urlpatterns = [
    # path('', catalog.as_view(), name='catalog')
    path('<str:mainurlname>', MainCategoryView.as_view(), name='maincategoryURL'),
    path('<str:mainurlname>/<str:suburlname>', SubCategoryView.as_view(), name='subcategoryURL')

]
