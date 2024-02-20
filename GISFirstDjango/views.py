from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'name': name})

def testview(request):
    # Do stuf
    a = 5
    b = 'yo'
    return render(request, "testtemplate.html", {'first': a,
                                                                    'second': b})
