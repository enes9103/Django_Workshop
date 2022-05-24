#!views,model,database
# views, models, database çift yönlü çalışıyor yani hem request hem response

#!codefirst
#codeu yazıp dtabase yollama

#!dbfirst 
#hazır databseden veriyi çekme

#!virtualenv
#Paketleri yönetmeye yarıyor.kolay yönetim
#Güncellenen sürümlerden projemizi korumak ve hata vermemesini sağlamak için kullanılır.
#olmasada olur ama best practice kullanılıyor

#!django __init__py
#python dosyası olduğunu tanımlamak için kullanılır.

#!proje ve app arasındaki fark
#blog projemiz var diyelim.içerisinde bir user app ve blog app olabilir.
#proje içeriisnde birden fazla app olabilir.
#app leri birden fazla projede kullanabiliriz

#!komutlar
#python -m venv env(base env kurduk)
#.\env\Scripts\activate(avtive ettik)

#pip install django(djangoyu yükledik)
#django-admin startproject fscohort1  . (içiçe olmadan proje başlatma komutu eğer nokta koymazsak projeyi içiçe klasör yapısıyla oluşturyor)
#pip freeze (yüklü paketleri listeler)
#python manage.py runserver (projeyi ayağa kaldırma default port 8000)
# python manage.py runserver 8080 (port numarasını değiştirme)
#python manage.py startapp student (student appı oluştrduk)

#from django.http import HttpResponse (django kütüphanesinden ekrana yazı yazmak için bunu import ediyoruz)