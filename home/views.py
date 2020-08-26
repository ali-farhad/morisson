from django.shortcuts import render
from home.models import Contact, Pricing, Jobs
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

import os.path

# Create your views here.


def index(request):
    if request.method == "POST":
        uname = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        msg = request.POST['message']

        rec = Contact(username=uname, phone=phone, email=email, message=msg)
        rec.save()
        messages.success(request, 'Your message has been received. We will be in touch with you shortly.')
    # return HttpResponseRedirect(reverse('home:index'))
        ref = request.META['HTTP_REFERER']
        refx = ref[-8:-1]
        if(refx == "contact"):
            return render(request, "home/contact.html")
        elif (refx == "careers"):
            return render(request, "home/careers.html")
        else:
            return render(request, "home/index.html")
    return render(request, "home/index.html")


def services(request):
    return render(request, "home/services.html")


def pricing(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        cname = request.POST['cname']
        phone = request.POST['phone']
        email = request.POST['email']
        checks = request.POST['drop']
        msg = request.POST['message']

        rec = Pricing(fname=fname, lname=lname, cname=cname,
                      phone=phone, email=email, checks=checks, message=msg)
        rec.save()
        messages.success(
            request, 'Your Offer has been received. We will be in touch shortly.')
        return HttpResponseRedirect(reverse('home:pricing'))
        # print(fname, lname, cname, phone, email, checks, msg)
    return render(request, "home/pricing.html")



def contact(request):
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


def careers(request):
    return render(request, "home/careers.html")


def apply(request):
    if request.method == "POST":
        uploaded_file = request.FILES['cv']
        fs = FileSystemStorage()
        ext = os.path.splitext(uploaded_file.name)[1]
        valid_exts = ['.pdf', '.doc', '.docx']
        if not ext.lower() in valid_exts:
            messages.success(
            request, 'Please upload valid PDF or Word file!')
            return HttpResponseRedirect(reverse('home:apply'))
        
        name = fs.save(uploaded_file.name, uploaded_file)
        
        url = fs.url(name)
        fname = request.POST['fname']
        phone = request.POST['phone']
        email = request.POST['email']
        rolee = request.POST['rolee']
        msg = request.POST['message']

        rec = Jobs(username=fname, phone=phone, email=email, role=rolee, message=msg, cv=url)
        rec.save()
        messages.success(
            request, 'Your Application has been received. We will be in touch with you shortly!')
        return HttpResponseRedirect(reverse('home:apply'))
        # print(fname, lname, cname, phone, email, checks, msg)
    
    return render(request, "home/apply.html")

