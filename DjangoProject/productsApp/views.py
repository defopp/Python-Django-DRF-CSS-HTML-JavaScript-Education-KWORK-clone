from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.forms.models import model_to_dict

from usersApp.models import User

from .models import MainCategory, SubCategory, DetailCategory, Product



# Create your views here.
class CatalogView(View):
    template_name = 'productsApp\\template\\catalog.html'
    def get(self, request):
        maincats = MainCategory.objects.all()
        subcats = SubCategory.objects.all()
        context = {
                'maincats':maincats,
                'subcats':subcats
                }
        return render(request, self.template_name, context)






class MainCategoryView(View):
    template_name = 'productsApp\\template\\category.html'
    
    def get(self, request, mainurlname):

        maincat = MainCategory.objects.filter(urlname=mainurlname)
        if maincat.exists():
            maincatQS = maincat.values_list('id', 'urlname', 'name', 'description')            
            for cat in maincatQS:
                mainid, urlname, name, description = cat

            subcat_list = get_list_of_subcategory(mainid)
            if len(subcat_list) > 0:     
                context = {
                    'maincategory' : {
                        'url': urlname,
                        'name': name,
                        'description': description, 
                        'subcat_list': subcat_list
                    }
                }
                return render(request, self.template_name, context)
            else:
                return HttpResponse(f'<h4>категория {name} не заполнена</h4>')
        else:
            return HttpResponse('404, такой категории не существует')





def get_list_of_subcategory(maincat_id:int) -> list: 
    subcatsSQ = SubCategory.objects.filter(main_category_id = maincat_id).values_list('id', 'urlname', 'name')
    subcatslist = []
    
    for cat in subcatsSQ:    
        subid, suburlname, subname = cat    
        if len(get_list_of_detailcategory(subid)) > 0:
            subcatslist.append({
                'name':subname,
                'url':suburlname,
                'detcat_list':get_list_of_detailcategory(subid)    
            })
        else:
            subcatslist.append({
                'name':subname,
                'url':suburlname    
            })
    return subcatslist

def get_list_of_detailcategory(subcat_id:int) -> list:  
    detailcatsSQ = DetailCategory.objects.filter(sub_category_id = subcat_id).values_list('id','urlname', 'sub_category_id', 'name')
    detcatlist = []   
                     
    for detcat in detailcatsSQ:
        id, url, sub_category_id, name  = detcat
        detcatlist.append({
            'id': id,
            'url': url,
            'subcat_id': sub_category_id,
            'name': name,
        })   
    return detcatlist


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
        

class new_project(View):
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
        detcat = DetailCategory.objects.get(name=project.detail_cat_id)
        subcat = SubCategory.objects.get(id=detcat.sub_category_id)
        maincat = MainCategory.objects.get(id=subcat.main_category_id)
        
        return render(request, self.template_name, context={
            'project':project,
            'owner':owner,
            'maincat': maincat,
            'subcat': subcat,
            'detcat': detcat,
        })