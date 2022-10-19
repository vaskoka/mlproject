from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from .models import Clabject, Attribute
from django.views import generic

class AttributeListView(generic.ListView):
    model = Attribute
    
    context_object_name = 'attribute_list'   # your own name for the list as a template variable
    queryset = Attribute.objects.all() # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AttributeListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = ''
        return context

class ClabjectListView(generic.ListView):
    model = Clabject
    
    
    context_object_name = 'clabject_list'   # your own name for the list as a template variable
    queryset = Clabject.objects.all() # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ClabjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['get_attributes'] = Attribute.objects.filter(clabject__name = clabject)
        return context
    

        

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clubjects = Clabject.objects.all().count()
    num_instances = Clabject.objects.all().count()

    # Available books (status = 'a')
    

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_clubjects': num_clubjects,
        'num_instances': num_instances,
        #'num_instances_available': num_instances_available,
        #'num_authors': num_authors,
        'new_project': new_project,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def new_project (request):
    return render (request, '',)