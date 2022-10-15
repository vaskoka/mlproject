from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
 #   return HttpResponse('Hello from Django!')

def index(request):
   
    return render('/index.html', context)

