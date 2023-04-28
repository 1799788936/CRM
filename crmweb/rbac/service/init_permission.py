#coding=utf-8

from crmweb import settings



def init_permission(current_user, request):
    permission_list = current_user.roles.filter(permission__isnull=False).values(
                                                                    "permission__id",
                                                                    "permission__title",
                                                                    "permission__is_menu",
                                                                    "permission__icon",
                                                                    "permission__url").distinct()
    
    menu_list = []
    permission_url_list = []
    for item in permission_list:
        if item["permission__is_menu"]:
            menu_list.append({
                'title': item["permission__title"], 
                "icon": item["permission__icon"], 
                "url": item["permission__url"]})
        permission_url_list.append(item['permission__url'])
    
    
    # permission_url_list = [ item['permission__url'] for item in permission_list]
    request.session[settings.PERMISSION_SESSION_KEY] = permission_url_list
    request.session[settings.MENU_SESSION_KEY] = menu_list
    