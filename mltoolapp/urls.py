from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('admin/mltoolapp/mlproject/add/', views.new_project, name='new_project'),

    
]

urlpatterns = [
    path('', views.index, name='index'),
    path('clabjects/', views.ClabjectListView.as_view(), name='clabjects'),
    path('clabject/<int:pk>', views.ClabjectDetailView.as_view(), name='clabject-detail'),
    path('attribute/<int:pk>', views.AttributeDetailView.as_view(), name='attribute-detail'),
    path('mldiagrams/', views.MLdiagramListView.as_view(), name='mldiagrams'),
    path('mldiagam/<slug:slug>/', views.MLDiagramDetailView.as_view(), name='mldiagram-detail'),
   
    
]

urlpatterns += [
   path('clabject/<int:pk>/instantiate/', views.instantiate_clabject, name='instantiate-clabject'),
   path('clabjectxxx/create/<int:pk>/create/', views.create_clabject_view, name='clabject-createxxx'),
   path('attributexxx/create/<int:pk>/create/', views.create_attribute_view , name='attribute-createxxx'),
   path('clabject/<int:pk>/instantiate/multiple-attributes/', views.create_multiple_attributes , name='create_multiple_attributes'),
   
]

# The create clubject wiew url
urlpatterns += [
#    path('clabject/create/', views.ClabjectCreate.as_view(), name='clabject-create'),
     path('clabject/<int:pk>/update/', views.ClabjectUpdate.as_view(), name='clabject-update'),
#    path('clabject/<int:pk>/delete/', views.ClabjectDelete.as_view(), name='clabject-delete'),
]

# The create Attribute wiew url
urlpatterns += [
    path('attribute/create/', views.AttributeCreate.as_view(), name='attribute-create'),
   # path('attribute/<int:pk>/update/', views.AttributeUpdate.as_view(), name='attribute-update'),
    #path('attribute/<int:pk>/delete/', views.AttributeDelete.as_view(), name='atribute-delete'),
]

# The create Ml diagram wiew url
urlpatterns += [
    path('mldiagram/create/', views.MLDiagramCreate.as_view(), name='mldiagram-create'),
   # path('mldiagram/<int:pk>/update/', views.MLDiagramUpdate.as_view(), name='mldiagram-update'),
    #path('mldiagram/<int:pk>/delete/', views.ClabjectDelete.as_view(), name='mldiagram-delete'),
]