from django.shortcuts import render, redirect


def guess_stock(request):
    '''
    This will redirect the url to the stock home page page
    :type request: HttpResponse
    :param request: Takes the request to show guess_stock.html
    
    '''
    return render(request, 'predictor/guess_stock.html')

def amazon_prediction(request):
    '''
    This will redirect the url to the amazon_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show amazon_predictionhtml
    
    '''
    return render(request, 'predictor/amazon_prediction.html')


def google_prediction(request):
    '''
    This will redirect the url to the google_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show google_prediction.html
    
    '''
    return render(request, 'predictor/google_prediction.html')


def microsoft_prediction(request):
    '''
    This will redirect the url to the microsoft_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show microsoft_prediction.html
    
    '''
    return render(request, 'predictor/microsoft_prediction.html')


def tesla_prediction(request):
    '''
    This will redirect the url to the tesla_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show tesla_prediction.html
    
    '''
    return render(request, 'predictor/tesla_prediction.html')

def facebook_prediction(request):
    '''
    This will redirect the url to the facebook_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show facebook_prediction.html
    
    '''
    return render(request, 'predictor/facebook_prediction.html')

def apple_prediction(request):
    '''
    This will redirect the url to the tesla_prediction page
    :type request: HttpResponse
    :param request: Takes the request to show apple_prediction.html
    
    '''
    return render(request, 'predictor/apple_prediction.html')


def csv_to_graph(request):
    '''
    This will redirect the url to the stock home page page
    :type request: HttpResponse
    :param request: Takes the request to show guess_stock.html
    
    '''
    return render(request, 'predictor/csv_to_graph.html')