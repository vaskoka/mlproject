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
    
    clabject_instance = get_object_or_404(Clabject, pk=pk)
    print(clabject_instance)
    
     # If this is a POST request then process the Form data
    if request.method == 'POST':
         # Create a form instance and populate it with data from the request (binding):
        form = InstantiateClabjectForm(request.POST, initial=clabject_instance.name)
        print(form)
         # Check if the form is valid:
        if form.is_valid():
            name = form.cleaned_data['yohoooo']
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # book_instance.due_back = form.cleaned_data['renewal_date']
            clabject_instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect('Thank you')
    
    else:
        form = InstantiateClabjectForm( )

        context = {
            'form': form,
            'clabject_instance': clabject_instance
    }
    return render(request, 'mltoolapp/instantiate_clabject.html', context)
       

    
    
