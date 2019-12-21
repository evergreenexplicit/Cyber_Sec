from django.urls import path, include,re_path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('register', views.register, name='register'),
        path('menu',views.menu,name='menu'),
        path('new_transaction', views.new_transaction, name='new_transaction'),
        path('new_transaction/confirm', views.confirm_transaction, name='confirm_transaction'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accept_panel', views.accept_panel, name='accept_panel'),
        re_path(r'accept/(?P<transid>\d+)$', views.accept_transaction, name='accept'),
]