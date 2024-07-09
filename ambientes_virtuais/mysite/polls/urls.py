from django.urls import path
from . import views

urlpatterns = [

    path('', views.registro_view, name='register'),  # Use 'registro_view' para a página de registro
    path('401/', views.error_401, name='error_401'),
    path('404/', views.error_404, name='error_404'),
    path('500/', views.error_500, name='error_500'),
    path('charts/', views.charts, name='charts'),
    path('layout-sidenav-light/', views.layout_sidenav_light, name='layout-sidenav-light'),
    path('layout-static/', views.layout_static, name='layout-static'),
    path('login/', views.login, name='login'),
    path('password/', views.password, name='password'),
    path('index/', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
]
