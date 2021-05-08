from django.shortcuts import render, redirect


def landing(request):
    '''
    This will redirect the url to the landing page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/landing.html')

def about(request):
    '''
    This will redirect the url to the about page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/about.html')

def contact(request):
    '''
    This will redirect the url to the contact page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/contact.html')

def services(request):
    '''
    This will redirect the url to the services page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    return render(request, 'home/services.html')
