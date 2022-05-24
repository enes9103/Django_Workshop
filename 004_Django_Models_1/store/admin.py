from django.contrib import admin
from store.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)



#! Admin işlemleri için Terminalde;
#1 python manage.py createsuperuser : Kullanıcı oluşturma
    #yaptıktan sonra sırayla name, surname, email, password, password2 gibi alanları doldurup kaydet. email gibi olmayan alan için enter ile geç.
#2 models.py dosyasında yapılan değişikliklerin browser admin dashboard da görünmesi için
    # admin.py dosyasında;
    #from store.models import Category  #import ediyoruz.
    #admin.site.register(Category)      # browser güncelle. Bu kısımda Category modelini admin panelinde görünür yapıyoruz.

#3 Admin dashboard da yapılan değişiklikleri Database de görmek için ya SQLite açıp proje içindeki SQLite dosyasını seçöiyoruz. Yada VSC de SQL Eklentisi ile DB dosyasına sağ tıklayıp DB ile aç diyoruz.