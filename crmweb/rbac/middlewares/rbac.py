# coding:utf-8
from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse
from crmweb import settings 

class RBACMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_url = request.path_info
        # print(current_url)
        for url in settings.VALID_URL_LIST:
            # reg = "^%s$" %url
            if re.match(url,current_url):
                return None
        
        permission_url_list = request.session[settings.PERMISSION_SESSION_KEY]
        if not permission_url_list:
            return HttpResponse("未获取到用户权限信息，请登录")
        flag = False
        # print(permission_url_list)
        for url in permission_url_list:
            reg = "^%s$" %url
            if re.match(reg,current_url):
                flag = True
                pass
        if not flag:
            return HttpResponse('无权访问')
        # return redirect('/customer/list/')