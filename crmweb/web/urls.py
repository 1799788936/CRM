from web.views import account
from web.views import customer
from web.views import payment
from django.urls import path

urlpatterns = [
    path('login/', account.login),
    path('customer/list/', customer.customer_list),
    path('customer/add/', customer.customer_add),
    path('customer/edit/', customer.customer_edit),
    path('customer/del/', customer.customer_del),
    path('customer/import/', customer.customer_import),
    # path(r'^customer/tpl/$', customer.customer_tpl),

    # path(r'^payment/list/$', payment.payment_list),
    # path(r'^payment/add/$', payment.payment_add),
    # path(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    # path(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),

]
