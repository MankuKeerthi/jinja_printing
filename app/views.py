from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='BTS and Army Forever'
    d={'BTS':data}
    return render(request,'data_render.html',context=d)
def login(request):
    d={'name':'Keerthi','age':21}
    return render(request,'login.html',context=d)
