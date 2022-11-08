from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
        # Add the attributes for this instance of the clabject in the context
        context['items'] = Attribute.objects.filter(clabject=clabject_obj)
        return context

class ClabjectCreate(CreateView):
    model = Clabject
    fields = ['name', 'subclassOf', 'instanceOf','potency','mldiagram']
    initial = {'name': 'Please enter a name'}

class ClabjectUpdate(UpdateView):
    model = Clabject
    fields = '__all__' # Not recommended (potential security issue if more fields added)
 
# Not used        
class ClabjectDelete(DeleteView):
    model = Clabject
    success_url = reverse_lazy('clabjects')
    

class AttributeCreate(CreateView):
    model = Attribute
    fields = ['clabject','name','data_type','value', 'potency']
    initial = {'name': 'Please enter a name'}

    
    
class AttributeUpdate(UpdateView):
    model = Clabject
    fields = '__all__' # Not recommended (potential security issue if more fields added)

# Not used in the present version
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
        # Add the clabjects and attributes to the context
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
    # Read the The mldiagram that will take the new clabject
    mldiagram = get_object_or_404(MLDiagram, pk=pk)
    data = {
        'mldiagram': mldiagram
    }
    if request.method == 'POST':
        form = CreateClabject(request.POST)
        # Validate and save the clabject as a new clabject
        if form.is_valid():
            new_clabject = form.save()
            return redirect('clabject-detail', new_clabject.id)
    else:
        # Create a form and bind the data to be submited 
        form = CreateClabject(data)
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
    # Get the clabject for the new attribute
    clabject = get_object_or_404(Clabject, pk=pk)
    data = {
        'clabject': clabject
    }
    if request.method == 'POST':
        form = CreateAttribute(request.POST)
        # It also validate that it has a value assigned if potency is 0
        if form.is_valid():
            form.save()
            return redirect('clabject-detail', clabject.id)
        else:
            # if potency is 0 and value to None throws ValidationError
            context = {
                'form':form,
                'data':data,
                'clabject':clabject
                }
            return render(request, 'mltoolapp/attribute_create.html', context)
    
    else:  
        # Create a form and bind the data
        form = CreateAttribute(data)
        context ={
        'form':form,
        'data':data,
        'clabject':clabject
    }
    return render(request, 'mltoolapp/attribute_create.html', context)
    


   
    """ Create multiple attributes is an inline formset that is a part of the instantiation of a clabject,
    once the new clabject instance is completed the form with all the existing attributes appears and allows adding or update attributes.
 
    """
def create_multiple_attributes(request, pk):
    clabject = Clabject.objects.get(pk=pk)
    AttributeInlineFormSet = inlineformset_factory(Clabject, Attribute,form=CreateAttribute, fields=('name','potency','value','data_type', ), extra=1)
    if request.method == "POST":
        formset = AttributeInlineFormSet(request.POST, instance=clabject)
        # for debugging - print in terminal
        print(formset.is_valid())
        print("FormsetAfter:   ",formset)
        print(formset.non_form_errors())
        if formset.is_valid():
            # for debugging - print in terminal
            print("FormsetAfter:   ",formset)
            formset.save()
            # Returns the same form with updated information
            return redirect('create_multiple_attributes', pk=pk)
    
    formset = AttributeInlineFormSet(instance=clabject)   
    return render(request, 'mltoolapp/create_multiple_attributes.html', {'formset': formset})
    








    """ Instantiate clubject takes a clabject and creates a new instance following the rules of multi level modeling.
    This is the first wiew of the instantiation.
    """
def instantiate_clabject(request, pk):
    # Get the clabject to be instantiated
    clabject_instance = get_object_or_404(Clabject, pk=pk)
    # create a list of all the attributes assosiated with this instance of the clabject
    attribute_list = Attribute.objects.filter(clabject=clabject_instance)
    # helper function to reduce potency by one
    def minus_one(num):
        if num >= 1:
            num = num-1
        return num
    # bind the data from the form
    data = {
            
            'potency': minus_one(clabject_instance.potency),
            'instanceOf': clabject_instance.id,
            'mldiagram':clabject_instance.mldiagram.id,
            'attribute_list':attribute_list
        }
        
     # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = CreateClabject(request.POST)
        if form.is_valid():
            # Save the new clabject
            new_clabject = form.save()
            for attribute in attribute_list:
                # Add the attributes to the new clabject, potency is reduced by one, attributes will be reviewed by the user in add/update form. 
                attribute.clabject = new_clabject
                new_attribute =Attribute(name=attribute.name, data_type=attribute.data_type, value=attribute.value, clabject=new_clabject, potency = minus_one(attribute.potency))
                new_attribute.save()
                
            return redirect('create_multiple_attributes', new_clabject.id, )
        else:
            context = {
                'form':form,
                'data':data,
                'clabject_instance': clabject_instance,
                'attribute_list':attribute_list
                }
            return render(request, 'mltoolapp/instantiate_clabject.html', context)
    else:
      
        form = InstantiateClabjectForm(data)
        context = {
            'form': form,
            'clabject_instance': clabject_instance,
            'attribute_list':attribute_list
            }
    return render(request, 'mltoolapp/instantiate_clabject.html', context)

       

    
    
