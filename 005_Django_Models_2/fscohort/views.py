from django.shortcuts import render                         #ORM sorguları views te  yapılır
from django.http import HttpResponse                        #Database den veriler burada çekilip render edilir.

def home(request):                                          #urls dosyasından çağrılan home fonksiyonu çağrılıp buradaki işlem yapılıyor.
    return HttpResponse('Welcome to the home page!')





#ORM Sorguları aynı zamanda shell terminalinden de yapılır.
#python manage.py shell