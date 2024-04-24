from .models import MainCategory, SubCategory, DetailCategory, Product



def get_sub_cats_with_det_cats(main_category_id:int) -> list:
    """list[dict{"subcat","det_cats_list"}] в случае успеха, 
    False в случае, если Субкатегории не найдены"""
    
    sub_categorys = SubCategory.objects.all().filter(main_category=main_category_id)
    if sub_categorys.exists():   
        
        # Если есть субкатегория у мейнкатегории, то ищем и отбираем детеилкатегорию
        # TODO ОТРЕФАКТОРИТЬ ЗАПРОС, ЧТОБЫ ПЕРЕБИРАТЬ НЕ ВСЕ ДЕТЕЛ КАТЕГОРИИ, А ТОЛЬКО СВЯЗАННЫЕС MAIN
        # TODO + переписать на генераторы списков 
        # TODO - попробовать генератор в генератиоре
        det_categorys = list(DetailCategory.objects.all())
         
        sub_cats_list = []
        for sub_cat in sub_categorys:
            det_cats_list = [det_cat for det_cat in det_categorys if det_cat.sub_category_id == sub_cat.id]
                    
            sub_cats_list.append({'sub_cat':sub_cat, 'det_cats_list':det_cats_list})  
    else:
        return False
    return sub_cats_list





def get_products_with_users_for_catalog() -> list:
    ...
     

# ТЕСТИРУЮ RAW
# products_list = list(Product.objects.raw('SELECT p.id, p.name AS project_name, p.price, p.owner_id as user_id,\
#                                                  u.username, u.avatar AS user_avatar\
#                                           FROM productsApp_product p\
#                                           INNER JOIN usersApp_user u ON p.owner_id = u.id\
#                                           WHERE p.sell_type = 1'))






















# ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА
# ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА
# ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА # ПОМОЙКА
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