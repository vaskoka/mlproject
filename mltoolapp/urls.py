from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/mltoolapp/mlproject/add/', views.new_project, name='new_project'),

    
]

urlpatterns = [
    path('', views.index, name='index'),
    path('clabject/', views.ClabjectListView.as_view(), name='clabject'),
    path('clabject/', views.AttributeListView.as_view(), name='attribute'),
]