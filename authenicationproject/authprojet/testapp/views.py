from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
@login_required

def java_page_view(request):
    return render(request,'testapp/javaexams.html')
def python_page_view(request):
    return render(request,'testapp/pythonexams.html')
def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexams.html')
