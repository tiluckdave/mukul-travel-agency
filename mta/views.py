from .models import Data, Contact, Tour_Packages
from django.contrib import messages
from django.shortcuts import render


def index(request):
    datas = Data.objects.all()
    tours = Tour_Packages.objects.all()
    params = {'home': datas, 'tour': tours}
    return render(request, 'index.html', params)


def about(request):
    datas = Data.objects.all()
    params = {'home': datas}
    return render(request, 'about.html', params)

def tours(request):
    tours = Tour_Packages.objects.all()
    datas = Data.objects.all()
    params = {'home': datas, 'tour': tours}
    return render(request, 'tours.html', params)

def singleTours(request, slug):
    tours = Tour_Packages.objects.all()
    datas = Data.objects.all()
    params = {'home': datas, 'tour': tours}
    return render(request, 'singletour.html', params)


def contact(request):
    # messages.error(request, 'Contact Form Submitted Successfully')
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name)<2 or len(email)<7 or len(phone)<10 or len(surname)<2:
            messages.error(request, "Please fill the details correctly")
        elif len(message)<10:
            messages.error(request, "Your message is too short")
        else:
            contact = Contact(first_name=name, last_name=surname, email_id=email, phone_number=phone, message=message)
            contact.save()
            messages.success(request, "Form has been submitted successfully")
    datas = Data.objects.all()
    params = {'home': datas}
    return render(request, 'contact.html', params)
