from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Home Page

    Args:
        request (): 

    Returns:
        HTTP Response: Html Files
    """
    # return HttpResponse('Hello, World ')
    return render(request, 'index.html')


def about(request):
    return HttpResponse('Your are in About Page')


def contact(request):
    return HttpResponse('Your are in contact Page')
