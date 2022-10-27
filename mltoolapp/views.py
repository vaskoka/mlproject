import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from traitlets import This
from mltoolapp.forms import InstantiateClabjectForm
from .models import Clabject, Attribute, MLDiagram
from django.views import generic


# Create your views here.

# Clabject views

class ClabjectListView(generic.ListView):
    model = Clabject
    paginate_by = 3
    
    context_object_name = 'clabject_list'   # your own name for the list as a template variable
    # template_name = 'clabject/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ClabjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['get_attributes'] = ''
        
        return context
    

class ClabjectDetailView(generic.DetailView):
    model = Clabject
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ClabjectDetailView, self).get_context_data(**kwargs)
        clabject_obj = self.object # this contain the object that the view is operating upon
        # Create any data and add it to the context
        context['items'] = Attribute.objects.filter(clabject=clabject_obj)
        return context

class ClabjectCreate(CreateView):
    model = Clabject
    fields = ['name', 'subclassOf', 'instanceOf','potency','mldiagram']
    initial = {'name': 'Please enter a name'}

class ClabjectUpdate(UpdateView):
    model = Clabject
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    
    
    
class ClabjectDelete(DeleteView):
    model = Clabject
    success_url = reverse_lazy('clabjects')
    

class AttributeCreate(CreateView):
    model = Attribute
    fields = ['clabject','name','data_type','value', 'potency']
    
    initial = {'name': 'Please enter a name'}



# Attributes views
class AttributeListView(generic.ListView):
    model = Attribute

class AttributeDetailView(generic.DetailView):
    model = Attribute
       
# ML diagram views    

class MLdiagramListView(generic.ListView):
    model = MLDiagram
    context_object_name = 'mldiagrams'
    template_name = 'mldiagram_list.html'
    

    
    
class MLDiagramDetailView(generic.DetailView):
    model = MLDiagram
          
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MLDiagramDetailView, self).get_context_data(**kwargs)
        mldiagram_obj = self.object # this contain the object that the view is operating upon
        # Create any data and add it to the context
        print("mldiagram_obj" , mldiagram_obj)
        # Return the clabject and attribute objects 
        clabject_items = Clabject.objects.filter(mldiagram=mldiagram_obj)
        attribute_items = Attribute.objects.all()
        context ['clabject_items'] = clabject_items
        context ['attribute_items'] = attribute_items
      
        return context 
              
    
# ML diagram forms   
class MLDiagramCreate(CreateView):
    model = MLDiagram
    fields = ['name']
    initial = {'name': 'Please enter a name'}
# Index page view         

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_mldiagrams = MLDiagram.objects.all().count()
    num_clabjects = Clabject.objects.all().count()
    num_attributes = Attribute.objects.all().count()

    # The 'all()' is implied by default.
    context = {
        'num_mldiagrams':num_mldiagrams,
        'num_clabjects': num_clabjects,
        'num_attributes': num_attributes,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)




def instantiate_clabject(request, pk):
    print("Request:    ",request)
    clabject_instance = get_object_or_404(Clabject, pk=pk)
    attribute_list = Attribute.objects.filter(clabject=clabject_instance)
    data = {
            
            'potency': int(clabject_instance.potency) -1,
            'instanceOf': clabject_instance.name,
            'mldiagram':clabject_instance.mldiagram,
            
        }
  
    
     # If this is a POST request then process the Form data
    if request.method == 'POST':
      
       
         # Create a form instance and populate it with data from the request (binding):
        # form = InstantiateClabjectForm(request.POST)
        data = request.POST
        print(data['name'])
        data['potency']
       #  Clabject(id=10, name='NewModel',potency=3, instanceOf_id=3, mldiagram_id=1,subclassOf_id=2 )
        new_clabject = Clabject(id=((clabject_instance.id)+random.randint(50, 500)+1), name=data['name'], potency = data['potency'],
                                instanceOf = clabject_instance, mldiagram=clabject_instance.mldiagram, subclassOf = clabject_instance.subclassOf)
       
        new_clabject.save()
        return HttpResponseRedirect(reverse('clabjects'))
        
    
    else:
        print(clabject_instance.instanceOf)
        print("goooooooooddd")
        form = InstantiateClabjectForm(data)

        context = {
            'form': form,
            'clabject_instance': clabject_instance,
            }
        print(context)
    return render(request, 'mltoolapp/instantiate_clabject.html', context)
       

    
    
