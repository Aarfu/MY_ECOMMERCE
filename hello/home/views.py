from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages#suse for flash messages
# Create your views here.
def index(request):
    #return HttpResponse("THIS IS HOME PAGE")
    # context={
    #     "variable":"variable 1 value send kar di h"
    # }

    return render(request,'index.html')

def about(request):
    # return HttpResponse("THIS IS ABOUT PAGE")
    return render(request,'about.html')
def services(request):
    # return HttpResponse("THIS IS SERVICES PAGE")
    return render(request, 'services.html')
def contact(request):
    # return HttpResponse("THIS IS CONTACTIC PAGE")
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')