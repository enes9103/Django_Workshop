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

# requirements.txt işlemleri
g. pip freeze > requirements.txt
        (yüklenen paketleri requirements.txt dosyasına atar.)
h. pip install -r requirements.txt
        (bir projede yüklü paketleri kendi projemize yüklemek için bu kodu çalıştırıyoruz.)

# App Models.py dosyasında yapılan her değişiklik için;
1. python manage.py makemigrations
        (Modelde Oluşturulan değişiklikleri bulup django da tanımlamamıza yarar)
2. python manage.py migrate
        (Yapılan değişiklikleri Veritabanında günceller)
        App lerin model.py dosyalarında yapılan her değişiklikten sonra bu iki işlem (i, j) yapılmalıdır.
        timezone.now Terminalde 1 ve 2 diye seçenekli bir soru sorarsa 1 seçip timezone.now yapacağız. Saat dilimi güncelleme

# Admin işlemleri için;
    # terminalde;
1. python manage.py createsuperuser : Kullanıcı oluşturma
    #yaptıktan sonra sırayla name, surname, email, password, password2 gibi alanları doldurup kaydet. email gibi olmayan alan için enter ile geç.
    # admin.py dosyasında;
2. models.py dosyasında yapılan değişikliklerin browser admin dashboard da görünmesi için
    #from store.models import Category  #import ediyoruz.
    #admin.site.register(Category)      # browser güncelle. Bu kısımda Category modelini admin panelinde görünür yapıyoruz.

3. Admin dashboard da yapılan değişiklikleri Database de görmek için ya SQLite açıp proje içindeki SQLite dosyasını seçöiyoruz.
    Yada VSC de SQL Eklentisi ile DB dosyasına sağ tıklayıp DB ile aç diyoruz.

# .env işlemleri
1. pip install python-decouple  : secret keyleri vs deployettiğimizde paylaşılmaması için bu kodu çalıştırıyoruz ve keylerimizi .env dosyasına taşıyoruz.

2. Bu komuttan sonra yapılacak işlem:
requirements.txt içine alıyoruz.  pip freeze > requirements.txt

3. Ana dizinde (manage.py olduğu dizin) .env dosyası oluşturuyoruz. Settings'den SECRET_KEY kopyalayıp .env dosyasına yapştırıyoruz. .env dosyasında tırnakları ve boşlukları siliyoruz.

4. from decouple import config : settings dosyasına ekliyoruz. (decouple import ettik)(13 14. satıra olabilir)

5. secret key satırını da SECRET_KEY = config("SECRET_KEY") olarak güncelliyoruz.

# Auth işlemleri
Authantication işlemleri için proje dosyası urls' path e aşağıdaki kod eklenerek auth işlemleri başlar.

1. path('accounts/', include('django.contrib.auth.urls'))
2. accounts işlemleri için templates altında registration adında klasör oluşturuyoruz.
3. registration clasörü altına accounts işlemleri için ihtiyaç duyduğumuz html templates lerini oluşturuyoruz. Örnek : login.html register.html vs.
4. login.html oluşturup login işlemi yaptıktan sonraredirect yönlendirme için Settings e eklememiz gereken bir kod var.
        LOGIN_REDIRECT_URL = 'home'   #nereye yönlendirmek istersek bu kod ile yönlendiriyoruz.
5. auth işlemleri için domaiin yanına /accounts/login/     /password_change/ vs yazılır dolaş
6. register işlemi için views.py dosyasında;
        a. from django.contrib.auth.forms import UserCreationForm    (oluşturmak için import sonrasında fonksiyonunu yazıyoruz)
        b. 




# Seçilen klasörde komutun çalışması için ve terminalde ilgili klasörde başlanması için settings/online services settings/cwd yazıyoruz Terminal>İntegrated alanına ${fileDirname}  ilgili ifade yazıllır.