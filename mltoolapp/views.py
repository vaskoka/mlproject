from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from mltoolapp.forms import CreateAttribute, CreateClabject, InstantiateClabjectForm
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
    template_name = 'attribute_create.html'
    '''
    def home(request):
        attribute = Attribute.objects.all()
        return render(request, 'attribute_create.html', {'attribute': attribute})
     '''
''' class CreateAttributeView(CreateView):
    # form_class = NewAttribute
    template_name = 'attribute_create.html'

    def form_valid(self, form):
        clabject = Clabject.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.clabject = clabject
        self.object.save()
    
     '''
class AttributeUpdate(UpdateView):
    model = Clabject
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class AttributeDelete(DeleteView):
    model = Clabject
    success_url = reverse_lazy('attributes')

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
    

    

    """ 
    Detail view of the MLdiagram model
    Returns:
        MLDiagram: the ML diagram
        Clabject: all the clabject items assosiated with the mldiagram
        Attribute: all the attributes assosiated with the clabject
        
    """
class MLDiagramDetailView(generic.DetailView):
    model = MLDiagram
          
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MLDiagramDetailView, self).get_context_data(**kwargs)
        mldiagram_obj = self.object # this contain the object that the view is operating upon
        # Return the clabject and attribute objects 
        clabject_items = Clabject.objects.filter(mldiagram=mldiagram_obj)
        attribute_items = Attribute.objects.all()
        context ['clabject_items'] = clabject_items
        context ['attribute_items'] = attribute_items
        return context 
              
 
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





    """ 
    Create a clabject using the CreateClabject form
    """   
def create_clabject_view(request, pk):
    mldiagram = get_object_or_404(MLDiagram, pk=pk)
    data = {
        'mldiagram': mldiagram
    }
    if request.method == 'POST':
        form = CreateClabject(request.POST)
        if form.is_valid():
            new_clabject = form.save()
            return redirect('clabject-detail', new_clabject.id)
    else:
        form = CreateClabject(data)
        print("The form object is:", form)
        context ={
        'form':form,
        'data':data,
        'mldiagram':mldiagram
    }   
    return render(request, 'mltoolapp/clabject_create.html', context)
 
    """ 
        Create an attribute using the CreateAttribute form
    """    
def create_attribute_view(request, pk):
    clabject = get_object_or_404(Clabject, pk=pk)
    data = {
        'clabject': clabject
    }
    if request.method == 'POST':
        form = CreateAttribute(request.POST)
        if form.is_valid():
            new_attribute = form.save()
            return redirect('clabject-detail', clabject.id)
    
    else:     
        form = CreateAttribute(data)
        context ={
        'form':form,
        'data':data,
        'clabject':clabject
    }
    return render(request, 'mltoolapp/attribute_create.html', context)
    







    """ _summary_
    """
def instantiate_clabject(request, pk):
    clabject_instance = get_object_or_404(Clabject, pk=pk)
    attribute_list = Attribute.objects.filter(clabject=clabject_instance)
    def minus_one(num):
        if num >= 1:
            num = num-1
        return num
    data = {
            
            'potency': minus_one(clabject_instance.potency),
            'instanceOf': clabject_instance.name,
            'mldiagram':clabject_instance.mldiagram,
            'attribute_list':attribute_list
        }
        
     # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        # form = InstantiateClabjectForm(request.POST)
        data = request.POST
        print(data['potency'])
        data['potency']
        try:
            new_clabject = Clabject( name=data['name'], potency = data['potency'],
                                instanceOf = clabject_instance, mldiagram=clabject_instance.mldiagram, subclassOf = clabject_instance.subclassOf)
       
            new_clabject.save()
            return HttpResponseRedirect(reverse('clabjects'))
        except:
            return HttpResponseRedirect(reverse('clabject-form'))
        
    
    else:
         # form = InstantiateClabjectForm(request.GET)
        print(clabject_instance.instanceOf)
        print("goooooooooddd")
        form = InstantiateClabjectForm(data)
        for attribute in attribute_list:
            attribute.potency = minus_one(attribute.potency)

        context = {
            'form': form,
            'clabject_instance': clabject_instance,
            'attribute_list':attribute_list
            }
        print(context)
    return render(request, 'mltoolapp/instantiate_clabject.html', context)
       

    
    
