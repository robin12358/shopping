from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     return  render(request, 'userside/index.html')
def detail(request):
     return render(request, 'userside/detail.html')
def contact(request):
     return render(request,'userside/contact.html')
def service(request):
     return render(request,'userside/service.html')
def offers(request):
     return render(request, 'userside/sale.html')
def shop(request):
     return render(request, 'userside/shoes.html')