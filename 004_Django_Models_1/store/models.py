from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)



#! App Models.py dosyasında yapılan her değişiklik için;
# 1. python manage.py makemigrations
#         (Modelde Oluşturulan değişiklikleri bulup django da tanımlamamıza yarar)
# 2. python manage.py migrate
#         (Yapılan değişiklikleri Veritabanında günceller)
#         App lerin model.py dosyalarında yapılan her değişiklikten sonra bu iki işlem (i, j) yapılmalıdır.
#         timezone.now Terminalde 1 ve 2 diye seçenekli bir soru sorarsa 1 seçip timezone.now yapacağız. Saat dilimi güncelleme