from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('admin/mltoolapp/mlproject/add/', views.new_project, name='new_project'),

    
]

urlpatterns = [
    path('', views.index, name='index'),
    path('clabjects/', views.ClabjectListView.as_view(), name='clabjects'),
    path('clabjects/<int:pk>', views.ClabjectDetailView.as_view(), name='clabject-detail'),
    path('mldiagrams/', views.ClabjectListView.as_view(), name='mldiagrams'),
    path('mldiagam/<int:pk>', views.MLDiagramDetailView.as_view(), name='mldiagram_detail'),
    
]

urlpatterns += [
    path('clabject/<uuid:pk>/instantiate/', views.instantiate_clabject, name='instantiate_clabject'),
]

# The create clubject wiew url
urlpatterns += [
    path('clabject/create/', views.ClabjectCreate.as_view(), name='clabject-create'),
    path('clabject/<int:pk>/update/', views.ClabjectUpdate.as_view(), name='clabject-update'),
    path('clabject/<int:pk>/delete/', views.ClabjectDelete.as_view(), name='clabject-delete'),
]