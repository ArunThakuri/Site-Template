from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services page")

def contact(request):
        if request.method == "POST":
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            contact = Contact(name=name, subject=subject, email=email, phone=phone, message=message, date=datetime.today())
            contact.save()
            messages.success(request, 'Your Form is Submitted.')
        return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")