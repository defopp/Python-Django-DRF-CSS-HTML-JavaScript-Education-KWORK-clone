from django.shortcuts import render, HttpResponse
from django.views import View
from django.forms.models import model_to_dict

from .models import MainCategory, SubCategory, DetailCategory


# Create your views here.
class MainCategoryView(View):
    template_name = 'productsApp\\template\\category.html'
    
    def get(self, request, urlname):
        # выбираем maincat
        maincat = MainCategory.objects.filter(urlname=urlname)
        if maincat.exists():
            maincatQS = maincat.values_list('id', 'urlname', 'name')            
            for cat in maincatQS:
                mainid, mainurlname, mainname = cat
            
            
            # выбираем subcat
            subcats = SubCategory.objects.filter(main_category_id = mainid)
            if subcats.exists():
                subcatsQS = subcats.values_list('id', 'urlname', 'name')
                
                #лист subcat
                subcatslist = []
                for cat in subcatsQS:      
                    subid, suburlname, subname = cat
                    
                    # выбираем detailcat
                    detailcats = DetailCategory.objects.filter(sub_category_id = subid)
                    if detailcats.exists():
                        detailcatsSQ = detailcats.values_list('urlname', 'sub_category_id', 'name')
                        
                        #лист detailcat
                        detcatlist = []
                        
                        for detcat in detailcatsSQ:
                            deturlname, subcatid, detname = detcat
                            
                            detcatlist.append({
                                'subcatid': subcatid,
                                'detname': detname,
                                'deturlname': deturlname,
                            })
                            
                        subcatslist.append({
                            'subname':subname,
                            'suburlname':suburlname,
                            'detcatlist':detcatlist    
                        })

                    else:
                        subcatslist.append({
                            'subname':subname,
                            'suburlname':suburlname    
                        })
                    
            context = {
                'maincategory' : {
                    'urlname': mainurlname,
                    'name': mainname,
                    'subcats': subcatslist, 
                }
            }
            return render(request, self.template_name, context)
        return HttpResponse('404')
    
    
    pass