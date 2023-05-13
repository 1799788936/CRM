from django.utils.deprecation import MiddlewareMixin
from rbac.models import UserInfo
from django.http import JsonResponse
import re

class RbacMiddleware(MiddlewareMixin):
    
    def process_request(self, request, *args, **kwargs):
        user = "wangcai"
        permission = request.method+" "+request.path
        user_obj = UserInfo.objects.filter(user_name=user)
        if not user_obj:
            return JsonResponse({"errors":"Authentication failed a"})
        permission_list = UserInfo.objects.get(user_name=user).role_id.filter().values(
            "permission_id__id",
            "permission_id__permission"
        ).distinct()

        for item in permission_list:
            if re.match(item["permission_id__permission"], permission):
                # print("权限认证成功")
                return 
        return JsonResponse({"errors":"Authentication failed"})