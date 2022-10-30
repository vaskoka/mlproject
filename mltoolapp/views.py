from attr import attributes
from django import forms
from django.forms import formset_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from mltoolapp.forms import CreateAttribute, CreateClabject, InstantiateClabjectAttributeForm, InstantiateClabjectForm
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
    #template_name = 'attribute_create.html'
    
    
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
        form = CreateAttribute(data)
        context ={
        'form':form,
        'data':data,
        'clabject':clabject
    }
    return render(request, 'mltoolapp/attribute_create.html', context)
    



def create_multiple_attributes(request,pk):
    clabject = get_object_or_404(Clabject, pk=pk)
    AttributeFormSet = modelformset_factory(Attribute, form=CreateAttribute)
    # helper function
    def minus_one(num):
        if num >= 1:
            num = num-1
        return num
    
    data =Attribute.objects.filter(clabject=clabject.instanceOf)
    
    for attribute in data:
        attribute.clabject = clabject
        attribute.potency = minus_one(attribute.potency) 
    print(data)

    #formset = AttributeFormSet(data)
    if request.method == 'POST':
        print("I am at this lineeeeee")
        formset = AttributeFormSet(request.POST, queryset=data)
        print("Formset valid: ",formset.is_valid())
        print("Formset bound: ",formset.is_bound)
        print("The formset:", formset)
        for form in formset:
            print("This is a form",form)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    print(form)
                    new_attr = form.save(commit=False)
                    new_attr.save
                    return redirect('clabject-detail', clabject.id)
        else:
           
            print(formset.errors)
            formset = AttributeFormSet(queryset=data)
        context ={
            'formset': formset,
            'data':data
           
        }
        
        return render(request,'mltoolapp/create_multiple_attributes.html', context )
        
    else:
        formset = AttributeFormSet(queryset=data)
        context ={
            'formset': formset,
            'data':data
           
        }
        
        return render(request,'mltoolapp/create_multiple_attributes.html', context )













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
            'instanceOf': clabject_instance,
            'mldiagram':clabject_instance.mldiagram,
            'attribute_list':attribute_list
        }
        
     # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = CreateClabject(request.POST)
        if form.is_valid():
            new_clabject = form.save()
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
        form = CreateClabject(data)
        context ={
        'form':form,
        'data':data,
        }
        form = InstantiateClabjectForm(data)
        context = {
            'form': form,
            'clabject_instance': clabject_instance,
            'attribute_list':attribute_list
            }
    return render(request, 'mltoolapp/instantiate_clabject.html', context)
       

    
    
