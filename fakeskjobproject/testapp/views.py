from django.shortcuts import render
from testapp.models import punejobs,hydjobs,mumbaijobs,banglorejobs

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def punejobss(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)

def hydjobss(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)


def mumbaijobss(request):
    jobs_list=mumbaijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/mumbaijobs.html',context=my_dict)


def banglorejobss(request):
    jobs_list=banglorejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/banglorejobs.html',context=my_dict)
