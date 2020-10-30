from django.urls import path

from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('create/', views.create_view, name='create'),
    path('lists/', views.list_view, name='lists'),
    path('<id>/', views.detail_view, ),
    path('<id>/update', views.update_view ),
    path('<id>/delete', views.delete_view,name='delete'),
]