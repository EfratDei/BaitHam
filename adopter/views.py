from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Animal.models import animal
from Event.models import event


def home(request):
    events =  event.objects.all().order_by('-id')[:2]
    if request.user.is_authenticated:
        animals = animal.objects.all()
    else:
        animals = animal.objects.filter(Adoption='Y')
    return render(request, 'adopter/home.html', {'animals': animals, 'events': events})


def reports(request):
    return render(request, 'adopter/reports.html')


def admin(request):
    return HttpResponseRedirect(reverse('admin:index'))


def contact_us(request):
    return render(request, 'adopter/contact_us.html')
