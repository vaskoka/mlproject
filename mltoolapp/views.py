from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from mltoolapp.forms import InstantiateClabject
from .models import Clabject, Attribute, MLDiagram
from django.views import generic


# Create your views here.

# Clabject views

class ClabjectListView(generic.ListView):
    model = Clabject
    paginate_by = 1
    
    context_object_name = 'clabject_list'   # your own name for the list as a template variable
    #queryset = Clabject.objects.all() # Get 5 books containing the title war
    template_name = 'clabject/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
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
        
        context['mldiagram_items'] = Clabject.objects.filter(mldiagram=mldiagram_obj)
        return context
    
# ML diagram forms   
class MLDiagramCreate(CreateView):
    model = MLDiagram
    fields = ['name']
    initial = {'name': 'Please enter a name'}
 
# class ClabjectUpdate(UpdateView):
  #  model = Clabject
   # fields = '__all__' # Not recommended (potential security issue if more fields added)

class ClabjectDelete(DeleteView):
    model = MLDiagram
    success_url = reverse_lazy('clabjects')   
    

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




# @permission_required('catalog.can_mark_returned', raise_exception=True)
def instantiate_clabject(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    clabject_instance = get_object_or_404(Clabject, pk=pk)

    # If this is a POST request then process the Form data
    request.method == 'GET'
        

        # Create a form instance and populate it with data from the request (binding):
    form = InstantiateClabject(request.GET)
    context = {
    'form': form,
    'clabject_instance': clabject_instance
    }
    return render(request, 'mltoolapp/instantiateClabject.html', context)
       
# Clbject forms   


class ClabjectCreate(CreateView):
    model = Clabject
    fields = ['name', 'subclassOf', 'instanceOf']
    initial = {'name': 'Please enter a name'}

class ClabjectUpdate(UpdateView):
    model = Clabject
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class ClabjectDelete(DeleteView):
    model = Clabject
    success_url = reverse_lazy('clabjects')
    
    
