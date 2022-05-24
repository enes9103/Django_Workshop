from django.urls import path
from .views import home                 #import edilen views.py dosyasının içindeki home fonksiyonunu kullanacağız.

urlpatterns = [
    path('', home, name='home'),        #home fonksiyonunu çağırır. "" boş olmaması durumunda burada yazan urls devamına /... şeklinde eklenmeli.
]



#! oluşturulan app main settings.py dosyasındaki INSTALLED_APPS değişkenine eklenir.