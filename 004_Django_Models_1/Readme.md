1. python -m venv env                   -environment oluşturma
2. .\env\Scripts\activate               -environment active yapma
3. pip install django                   -django yükleme
4. django-admin startproject main .     -proje başlatma (main yazan yere proje ismi yaz)
5. python manage.py runserver           -server'ı local host ta çalıştırmak için kullanılır. ctrl+c ile sonlandırılır.
6. python manage.py startapp student    -app oluşturmak için kullanılır. (student yerine istediğimiz app adını yazabiliriz.)



a. python --version
b. Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
        (kurulum 2. adımda (activate) security error hatası alırsak bu komutu uygula )
c. pip list
        (django yüklü mü görebiliriz.)
d. pip freeze
        (django yüklü mü görebiliriz. list ve freeze farkı sadece formatları değişik)
e. python -m pip install --upgrade pip
        (django versiyonunu upgrade etmek istersek kullanabiliriz.)
f. python manage.py runserver 8080
        (server default olarak 8000 portunda açar ancak 8080 gibi bir port belirterek istediğimiz portta da açmasını sağlayabiliriz.)
g. pip freeze > requirements.txt
        (yüklenen paketleri requirements.txt dosyasına atar.)
h. pip install -r requirements.txt
        (bir projede yüklü paketleri kendi projemize yüklemek için bu kodu çalıştırıyoruz.)

# App Models.py dosyasında yapılan her değişiklik için;
i. python manage.py makemigrations
        (Modelde Oluşturulan değişiklikleri bulup django da tanımlamamıza yarar)
j. python manage.py migrate
        (Yapılan değişiklikleri Veritabanında günceller)
        App lerin model.py dosyalarında yapılan her değişiklikten sonra bu iki işlem (i, j) yapılmalıdır.
        timezone.now Terminalde 1 ve 2 diye seçenekli bir soru sorarsa 1 seçip timezone.now yapacağız. Saat dilimi güncelleme

# Admin işlemleri için Terminalde;
#1 python manage.py createsuperuser : Kullanıcı oluşturma
    #yaptıktan sonra sırayla name, surname, email, password, password2 gibi alanları doldurup kaydet. email gibi olmayan alan için enter ile geç.
#2 browser dashboard da yapılan değişiklik görünmesi için : admin.py dosyasında 
    #from store.models import Category
    #admin.site.register(Category)      # browser güncelle. Bu kısımda Category modelini admin panelinde görünür yapıyoruz.

