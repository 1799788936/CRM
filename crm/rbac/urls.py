from django.contrib import admin
from django.urls import path, re_path
from rbac.views import role, userinfo, permission

urlpatterns = [
    re_path('^role_list/$', role.RoleView.as_view()),
    # re_path(r'role_list_view/(?P<pk>\d+)', role.RoleViewPk.as_view()),
    re_path('role_list/(?P<pk>\d+)', role.RoleViewPk.as_view()),
    re_path('^userinfo_list/$', userinfo.UserInfoView.as_view()),
    re_path('userinfo_list/(?P<pk>\d+)', userinfo.UserInfoViewPk.as_view()),
    re_path('^permission_list/$', permission.PermissionView.as_view()),
    re_path('^permission_list/(?P<pk>\d+)$', permission.PerMissionViewPk.as_view()),
    # re_path('userinfo_list/$', permission.PermissionView.as_view()),
]
