from django.shortcuts import render, HttpResponse
from django.views import View
from django.forms.models import model_to_dict

from .models import MainCategory, SubCategory, DetailCategory


# Create your views here.
class MainCategoryView(View):
    template_name = 'productsApp\\template\\category.html'
    
    def get(self, request, urlname):

        maincat = MainCategory.objects.filter(urlname=urlname)
        if maincat.exists():
            maincatQS = maincat.values_list('id', 'urlname', 'name')            
            for cat in maincatQS:
                mainid, urlname, name = cat

            subcat_list = get_list_of_subcategory(mainid)
            if len(subcat_list) > 0:     
                context = {
                    'maincategory' : {
                        'urlname': urlname,
                        'name': name,
                        'subcat_list': subcat_list, 
                    }
                }
                return render(request, self.template_name, context)
            else:
                return HttpResponse(f'категория <h4>{name}</h4> не заполнена')
        return HttpResponse('404')
    pass





def get_list_of_subcategory(maincat_id:int) -> list:
    
    subcatsSQ = SubCategory.objects.filter(main_category_id = maincat_id).values_list('id', 'urlname', 'name')
    subcatslist = []
    
    for cat in subcatsSQ:    
        subid, suburlname, subname = cat
        
        if len(get_list_of_detailcategory(subid)) > 0:
            subcatslist.append({
                'name':subname,
                'urlname':suburlname,
                'detcat_list':get_list_of_detailcategory(subid)    
            })
        else:
            subcatslist.append({
                'name':subname,
                'urlname':suburlname    
            })
    
    return subcatslist






def get_list_of_detailcategory(subcat_id:int) -> list:
    
    detailcatsSQ = DetailCategory.objects.filter(sub_category_id = subcat_id).values_list('urlname', 'sub_category_id', 'name')
    detcatlist = []   
                     
    for detcat in detailcatsSQ:
        url, sub_category_id, name  = detcat
        detcatlist.append({
            'url': url,
            'subcat_id': sub_category_id,
            'name': name,
        })
        
    return detcatlist