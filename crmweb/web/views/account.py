# coding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from rbac import models 
from rbac.service.init_permission import init_permission

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user', '')
    passwd = request.POST.get('pwd', '')
    current_user = models.UserInfo.objects.filter(name=user, password=passwd).first()
    if not current_user:
        return HttpResponse('用户名或密码错误')
    request.session['user'] = user
    init_permission(current_user, request)
    return redirect('/customer/list/')