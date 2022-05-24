1. python -m venv env                   -environment oluşturma
2. .\env\Scripts\activate               -environment active yapma
3. pip install django                   -django yükleme
4. django-admin startproject main .     -proje başlatma (main yazan yere proje ismi yaz)
5. python manage.py runserver           -server'ı local host ta çalıştırmak için kullanılır. ctrl+c ile sonlandırılır.
6. python manage.py startapp student    -app oluşturmak için kullanılır. (student yerine istediğimiz app adını yazabiliriz.)



a. python --version
b. Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted (2. adımda (activate) security error hatası alırsak bu komutu uygula )
c. pip list (django yüklü mü görebiliriz.)
d. pip freeze (django yüklü mü görebiliriz. list ve freeze farkı sadece formatları değişik)
e. python -m pip install --upgrade pip (django versiyonunu upgrade etmek istersek kullanabiliriz.)
f. python manage.py runserver 8080 (server default olarak 8000 portunda açar ancak 8080 gibi bir port belirterek istediğimiz portta da açmasını sağlayabiliriz.)