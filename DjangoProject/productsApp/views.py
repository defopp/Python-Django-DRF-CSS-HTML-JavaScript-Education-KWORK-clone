from django.shortcuts import render, HttpResponse, redirect
from django.views import View


from usersApp.models import User
from .models import MainCategory, SubCategory, DetailCategory, Product
from .services import *



# Create your views here.
class CatalogView(View):
    template_name = 'productsApp\\template\\catalog.html'
    def get(self, request):
        maincats = MainCategory.objects.all()
        subcats = SubCategory.objects.all()
        return render(request, self.template_name, context = {'maincats':maincats,
                                                              'subcats':subcats})


class MainCategoryView(View):
    template_name = 'productsApp\\template\\category.html'
    
    def get(self, request, mainurlname):      
        
        # Проверка наличия категории по "mainurlname"
        try:
            main_category = MainCategory.objects.get(urlname=mainurlname)
        except:
            return HttpResponse('404, такой категории не существует')         
        
        sub_cats_with_det_cats = get_sub_cats_with_det_cats(main_category.id)

        if sub_cats_with_det_cats is not False:    
            context = {
                'main_cat':main_category,
                'sub_cats_list':sub_cats_with_det_cats
                }
            return render(request, self.template_name, context)
        else:
            return HttpResponse(f'Категория "{main_category}" не заполнена')         
        
        
        
class SubCategoryView(View):
    template_name = 'productsApp\\template\\category_catalog.html'

    def get(self, request, mainurlname, suburlname):
        
        maincat = MainCategory.objects.filter(urlname=mainurlname)
        if maincat.exists():
            maincatQS = maincat.values_list('id', 'urlname', 'name')
            for cat in maincatQS:
                mainid, mainurlname, mainname = cat
                
             
            subcat = SubCategory.objects.filter(main_category_id = mainid, urlname = suburlname)
            if subcat.exists():
                subcatQS = subcat.values_list('id', 'urlname', 'name')
                for cat in subcatQS:
                    subid, suburlname, subname = cat
                    products = Product.objects.all().filter(sub_cat_id = subname)
                    users = User.objects.all()
                    
                if len(get_list_of_detailcategory(subid)) > 0:
                    context = {
                        'maincategory': {
                            'id':mainid,
                            'url':mainurlname,
                            'name':mainname,
                            'subcategory': {
                                'id':subid,
                                'url':suburlname,
                                'name':subname,
                                'detailcategory': get_list_of_detailcategory(subid)
                            }
                        },
                        'products': products,
                        'users': users
                    }
                    return render(request, self.template_name, context)
                else:
                    return HttpResponse('У Sub категории не заполнены detail категории')
            else:    
                return HttpResponse('Такой Sub категории не существует')
        else:
            return HttpResponse('Такой MAIN категории не существует')
        
            
class new_projectView(View):
    template_name = 'productsApp\\template\\project_create.html'
    def get(self, request):
        
        if request.user.is_authenticated:
            context = {
                'maincats':MainCategory.objects.all(),
                'subcats':SubCategory.objects.all(),
                'detcats':DetailCategory.objects.all()
            }
            return render(request, self.template_name, context)
        else:
            return redirect('signup')
    
    def post(self, request):
        post = request.POST
        if request.user.is_authenticated:
            
            sub_cat_id = SubCategory.objects.get(id=DetailCategory.objects.get(name = post['detcat']).sub_category_id).name
            main_cat_id = MainCategory.objects.get(id=SubCategory.objects.get(id=DetailCategory.objects.get(name = post['detcat']).sub_category_id).main_category_id)
            
            product = Product(sell_type=post['type'], 
                              name=post['name'], 
                              description=post["description"], 
                              detail_cat_id=post['detcat'], 
                              price=post["price"],
                              owner_id=request.user.id,
                              sub_cat_id=sub_cat_id,
                              main_cat_id=main_cat_id)
            product.save()
            
            return redirect('project', project_id = product.id)
        
        
class ProjectView(View):
    template_name = 'productsApp\\template\\project.html'
    def get(self, request, project_id):
        project = Product.objects.get(id=project_id)
        owner = User.objects.get(id=project.owner_id)
        owner_products = Product.objects.all().filter(owner_id=owner.id)
        detcat = DetailCategory.objects.get(name=project.detail_cat_id)
        subcat = SubCategory.objects.get(id=detcat.sub_category_id)
        maincat = MainCategory.objects.get(id=subcat.main_category_id)
        
        return render(request, self.template_name, context={
            'project':project,
            'owner':owner,
            'owner_products': owner_products,
            'maincat': maincat,
            'subcat': subcat,
            'detcat': detcat,
        })