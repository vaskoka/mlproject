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
    path('mldiagams/', views.MLdiagramListView.as_view(), name='mldiagrams'),
    path('mldiagam/<slug:slug>/', views.MLDiagramDetailView.as_view(), name='mldiagram_detail'),
    
]

urlpatterns += [
   path('clabject/<uuid:pk>/instantiate/', views.instantiate_clabject, name='instantiate_clabject'),
]

# The create clubject wiew url
urlpatterns += [
    path('clabject/create/', views.ClabjectCreate.as_view(), name='clabject_create'),
    path('clabject/<int:pk>/update/', views.ClabjectUpdate.as_view(), name='clabject_update'),
    path('clabject/<int:pk>/delete/', views.ClabjectDelete.as_view(), name='clabject_delete'),
]

# The create Ml diagram wiew url
urlpatterns += [
    path('mldiagram/create/', views.MLDiagramCreate.as_view(), name='mldiagram_create'),
    path('mldiagram/<int:pk>/update/', views.ClabjectUpdate.as_view(), name='mldiagram_update'),
    path('mldiagram/<int:pk>/delete/', views.ClabjectDelete.as_view(), name='mldiagram_delete'),
]