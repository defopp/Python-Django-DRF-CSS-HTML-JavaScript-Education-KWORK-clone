from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from tools import if_login

from usersApp.models import User
from .models import MainCategory, SubCategory, DetailCategory, Product
from .services import *



# Create your views here.
class CatalogBuyView(View):
    template_name = 'productsApp/template/catalog_buy.html'
    def get(self, request):
        maincats = MainCategory.objects.all()
        subcats = SubCategory.objects.all()
        return render(request, self.template_name, context = {'maincats':maincats,
                                                              'subcats':subcats})


class CatalogSellView(View):
    template_name = 'productsApp/template/catalog_sell.html'

    def get(self, request):
        projects_list = Product.objects.all().filter(sell_type=0)
        return render(request, self.template_name, context={'projects_list':projects_list})




class MainCategoryView(View):
    template_name = 'productsApp/template/category.html'
    
    def get(self, request, mainurlname):      
        
        # Проверка наличия категории по "mainurlname"
        try:
            main_category = MainCategory.objects.get(urlname=mainurlname)
        except:
            return HttpResponse('404, такой категории не существует')         
        
        # Проверка/сборка, есть ли субкатегории у мейнкатегории
        sub_cats_with_det_cats = get_sub_cats_with_det_cats(main_category.id)
        if sub_cats_with_det_cats is not False:
            return render(request, self.template_name, {'main_cat':main_category,
                                                        'sub_cats_list':sub_cats_with_det_cats})
        else:
            return HttpResponse(f'Категория "{main_category}" не заполнена')         
        
        
        
class SubCategoryView(View):
    template_name = 'productsApp/template/category_catalog.html'

    def get(self, request, mainurlname, suburlname):
        
        # Получить МЕЙНКАТЕГОРИЮ, получить СУБКАТЕГОРИЮ и все ДЕТЕЙЛКАТЕГОРИИ
        try:
            main_category = MainCategory.objects.get(urlname=mainurlname)
            sub_category = SubCategory.objects.get(urlname=suburlname)
        except: return HttpResponse('404, такой категории не существует')
        
        det_categorys_list = list(DetailCategory.objects.filter(sub_category=sub_category.id))
        if len(det_categorys_list) != 0:
            
            # Далее получаешь все продукты по СУБКАТЕГОРИИ
            products_list = Product.objects.all().select_related('owner').filter(sell_type=1, sub_cat=sub_category)       
            return render(request, self.template_name, {'main_cat':main_category,
                                                        'sub_cat':sub_category,
                                                        'det_cats_list':det_categorys_list,
                                                        'products_list':products_list})
        else: return HttpResponse('У подкатегори не заполнены detail категории')
        
      
            
class new_projectView(View):
    template_name = 'productsApp/template/project_create.html'
    
    @if_login
    def get(self, request):
        return render(request, self.template_name, {'maincats':MainCategory.objects.all(),
                                                    'subcats':SubCategory.objects.all(),
                                                    'detcats':DetailCategory.objects.all()})
    
    @if_login
    def post(self, request):
        # TODO: Форму от модели и валидацию
        product = Product(sell_type=request.POST['type'], 
                            name=request.POST['name'], 
                            description=request.POST["description"], 
                            detail_cat_id=request.POST['detcat'], 
                            price=request.POST["price"],
                            owner_id=request.user.id,
                            sub_cat_id=SubCategory.objects.get(id=DetailCategory.objects.get(name = request.POST['detcat']).sub_category_id).name,
                            main_cat_id=MainCategory.objects.get(id=SubCategory.objects.get(id=DetailCategory.objects.get(name = request.POST['detcat']).sub_category_id).main_category_id))
        product.save()    
        return redirect('project', project_id = product.id)
        
       
            
            
             
class ProjectView(View):
    template_name = 'productsApp/template/project.html'
    
    # TODO Обновить модель продукта, и запрос к моделям категорий.
    def get(self, request, project_id):    
        try: project = Product.objects.select_related('owner', 'detail_cat', 'sub_cat', 'main_cat').filter(id=project_id).get()
        except: return HttpResponse('Такого проекта не существует')
        
        context = {"project":project}        
        
        owner_projects = list(Product.objects.all().select_related('owner').filter(owner=project.owner.id))
        if len(owner_projects) != 0: context['owner_projects'] = owner_projects    
           
        return render(request, self.template_name, context)

        
