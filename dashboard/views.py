from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from  . import views
# Create your views here.
@login_required
def index(request):
    return render(request,'dashboard/page/index.html')
def adlogin(request):
    if request.method == "GET":
        return render(request,'dashboard/page/signin.html')
    elif request.method =='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user =authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('adhome'))
        else:
            return HttpResponseRedirect(reverse('adlogin'))

@login_required
def adlogout(request):
    logout(request)
    context={
        'message': 'Successfully  Logout'
    }
    return render(request, 'dashboard/page/signin.html', context)
@login_required
def dashboard(request):
    return render(request,'dashboard/page/index.html')

@login_required
def profile(request):
    return render(request,'dashboard/page/profile.html')