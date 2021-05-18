from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect,reverse
from home.forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from predictor.views import guess_stock


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

def signup(request):
    '''
    This will redirect the url to the signup
    :type request: HttpResponse
    :param request: Takes the request to show signup.html
    '''
    if request.user.is_authenticated:
        return redirect('guess_stock')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)  
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Account Successfully Created !')
            return redirect('signin')
        context = {'form':form}
    return render(request, 'home/signup.html', context)


def signin(request):
    return render(request,'home/signin.html')


def signin(request):
    '''
    This will redirect the url to the signin
    :type request: HttpResponse
    :param request: Takes the request to show signin.html
    
    '''
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("guess_stock")
                else:
                    messages.success(request, 'Invalid login !')

            else:
                messages.success(request, 'Wrong Username and Password !')

    else:
        form=LoginForm()
    return render(request,"home/signin.html",{"form":form})


@login_required
def signout(request):
    '''
    This will redirect the url to the landing page
    :type request: HttpResponse
    :param request: Takes the request to show landing.html
    
    '''
    logout(request)
    return HttpResponseRedirect(reverse('landing-page'))