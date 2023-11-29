from django.shortcuts import render
from app3.models import *
from app3.form import *

# Create your views here.
def base(request):
    return render(request,'base.html')
def upload(request):
    form=bookform()
    if(request.method=='POST'):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return base(request)
    return render(request,'add_book.html',{'form':form})   
def booklist(request):
    b=Book.objects.all()
    return  render(request,'list.html',{'b':b})

def edit_item(request,p):
   b=Book.objects.get(pk=p)
   form=bookform(instance=b)
   if (request.method=='POST'):
       form=bookform(request.POST,instance=b)
       if form.is_valid():
            form.save()
            return base(request)
   return render(request,'edit.html',{'form':form}) 
