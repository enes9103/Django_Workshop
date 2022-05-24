import os                                                       # terminali temizlemek için kullanılan kod barry hoca tarafından yazılmıştır.
os.system('cls' if os.name == 'nt' else 'clear')

# def print_type(data):
#     for i in data:
#         print(i, type(i))

# test = [122, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]
# print_type(test)
#!......................................................................
# class Person:                 #class attribute
#     name = 'Barry'
#     age = 45

# person1 = Person()            #instance attribute
# person2 = Person()

# print(person1.name)           #Barry
# print(person2.name)          #Barry

# Person.job = 'teacher'

# print(person1.job)            #teacher
                                #class'ta yapılan değişiklik instance'larda da etkili olur.

#! class attributes vs instance attributes
# person1.location = 'Turkey'
# # print(person2.location)             #location'ının değeri None'dur. çünkü bir instance da yapılan değişiklik diğer instance da etkili değildir.
# person2.name = 'Aaron'
# print(person1.name)                   #Barry verir çünkü instance'larda yapılan değişiklik sadece o instance'a etkili olur.

#! SELF keyword

# class Person:
#     name = 'Barry'
#     age = 45

#     def test(self):                       #self keyword'u ile instance'a ait değişkenleri kullanabiliriz.
#         print('test')                     #self yerine person1 koymuş olduk.

#     def set_details(self, name, age):     #self keyword'u ile instance'a ait değişkenleri kullanabiliriz.
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person()
# person1.test()
# Person.test(person1)                      #Django arka tarafta aslında bu koda çevirir.

# person1.get_details()                     #Barry 45 verir. çünkü class'a ait değişkenleri kullanır. Hala set details func çalıştırılmadı.
# person1.set_details('Aaron', 37)
# person1.get_details()                     #Aaron 37 verir. çünkü instance'a ait değişkenleri kullanır.

#! static method
##Django da işimize çok fazla yaramayacak bir method.
# class Person:
#     company = 'Clarusway'                 #ortak özellikler class attribute'te tanımlanır.

#     def set_details(self, name, age):     
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod                         #static method'u kullanmak için @staticmethod decorator yazılıp kullanılır.
#     def salute():                         #classtan da bağımsız bir methoddur. instance ile bağlantı kurmaya gerek yoktur.
#         print('Hi there!')

# # print(Person.name)

# person1 = Person()
# person1.salute()                          #Hi there! instance ile bağlantı kurmaya gerek olmadığı için self kullanmadık.

#! special methods   (__init__ ve __str__)
# class Person:
#     company = 'Clarusway'
                                            #constructor yapısı
#     def __init__(self, name, age):        #method otomatik kendisi çalışır. __init__ sabit isimli bir method dur.
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person('Barry',45)              #person1 instance tanımlanır tanımlanmaz özellikler de parametre olarak verildi.
                                            #person1 tanımlanır tanımlanmaz classs a bakar ve init fonksiyonu varmı kontrol eder ve __init__ method'u çalıştırılır. burada init methodu içindeki istenen parametreleri göndermek zorundayız yoksa hata verir.
# person1.get_details()                     #Barry 45 verir.

# liste = [4,2,9,11,5]
# print(liste)                              #[4, 2, 9, 11, 5]
# print(person1)                            #85. satırdaki methodu yazmazsak on the air sonuç döndürür.
                                            #__str__ methodu yazılmış ise name ve age'i person1 instance'ından çeker ve onu çalıştırır.
# print(person1.__str__())                  #Django aslında arkada bu işlemi yapmış olur. bizim str tanımlayıp person1 yazdırmamız ile aynı sonucu döndürür.
##!! OOP (Object Oriented Programing) PRENSİPLERİ (encapsulation, abstraction, inheritance, polymorphism)
#! encapsulation and abstraction
    ## encapsulation: Veriyi gizlemek için kullanılan yöntem.
    ## abstraction: Kullanıcıyı gereksiz detaylardan soyutlama.
# class Person:
#     company = 'Clarusway'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000                   #_id private attribute Bunu değiştirmeyin değiştirirseniz düüzgün çalışmaz demektir.Fiziki koruma sağlamıyor.
#         self.__id2 = 4000                 #__id2 kısmen koruma sağlıyor. __id2 print edildiğinde attribute error verir.

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1= Person('Aaron',37)
# print(person1._id)                        #5000 id'yi erişip kullanılabiliyor.
# # print(person1.__id2)                    #AttributeError: 'Person' object has no attribute '__id2' __id2 'ye erişim yok. Ancak !!
# print(person1._Person__id2)               #4000, yasak yok ama illa erişmek istiyorsanız bu şekilde yine de id ye erişebilirsiniz. id'yi erişip kullanılabiliyor.

# liste = [4,2,9,11,5]
# liste.sort()                              #arkada sort methodu kullanılır. Ancak biz bunun nasıl yapıldığını görmeyiz. Kullanıcı gereksiz detaylardan soyutlanır. Buna abstract OOP prensibi denir..
# print(liste)                              #[2, 4, 5, 9, 11]
                                            #absract OOP örneğin, whatsapp mesajını yazdığımızda biz iki mavi tik görüyoruz. Arkada yazdığımız mesaj makina diline çevriliyor. gidecek kullanıcı adresi bulunuyor vs hiçbirini görmüyoruz.
#! inheritance and polymorphism
    ## inheritance: Miras. Bir class'ın başka bir class'ının özelliklerini kullanmak için kullanılır. 
    ## polymorphism: Birden fazla class'ın aynı özelliklerini kullanmak için kullanılır.

class Person:
    company = 'Clarusway'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_details(self):
        print(self.name, self.age)

class Lang:
    def __init__(self,langs):
        self.langs = langs

    def display_langs(self):
        print(self.langs)

class Employee(Person, Lang):                       #Aynı olan elemanları aynısın ı yazmaktansa parentından alır. Yeni değişkenler için yeni init tanımlarız. Burada employee class ı person ve lang classlarını miras aldı kullandı ve aşağıda yeni özellikler de ekledi.
    def __init__(self, name, age, path, langs): 
        # self.name = name                          #Bu şekilde yazıp aynı elemanları tekrar da yazabiliriz ancak genel kabul gören aşttaki gibi super ile parent a gönderip oradan çekmektir.
        # self.age = age
        super().__init__(name,age)                  #super() methodu ile parent class'ının init methodunu çağırıyoruz. super() ilk parent class'ının init methodunu çağırıyor. name ve age değişkenlerini Person class'ından miras aldık.
        self.path = path                            #path değişkeni lazım olduğu için onu burada bu class ta kendimiz tanımladık.
        Lang.__init__(self, langs)                  #Lang class'ını miras aldık. Yani langs değişkenini kullanıyoruz. super() ile ilk class ı inherit ettiğimiz için ikincide ve sonraki class lar için  ismen çağırırız. langs ler lazımdı onu da lang clasından kullanmak için miras almış olduk
        # self.langs = langs
                                                    #Özetle: yeni bir class oluştururken aynı bir önceki classtan aynı verileri kullanma ihtiyacı varsa parent class olarak bu verileri miras alıp diğer ihtiyacımız olan verileri yeni classta tanımlarız.. Kullanırken de bu classtakileri direk, parent classtakileri super().__init__ ile parenct classtan miras alıp kullanabiliriz.
    
    # Polimorphism: Miras aldığımız class ları aynen kullanmak yerine değiştirerek kullanma demek diyebiliriz. Override da bu işlemin yapılışı
    #! override: Mevcut haliyle bir classs işimize yarıyorsa bunu alıp ilave yetenekler işlevler ekleyerek kullanabiliriz. Örneğin aşağıda super() ile parent class'ı aldık ve ilave olarak self.path yazdırma ihtiyacımız vardı ayrıca onu da yaptık.
    def get_details(self):
        # print(self.name, self.age, self.path)     #Bu şekilde yazıp aynı elemanları tekrar da yazabiliriz ancak genel kabul gören aşttaki gibi super ile parent a gönderip oradan çekmektir. Oradan çekip başka ihtiyaçlar varsa alttaki gibi onları eklesek yeterli
        super().get_details()                       #burada Person class ının get_details ını aldık ve aynı işlevlerin yanında ihtiyacımız olan print(self.path) işlevini de ekledik. 
        print(self.path)

emp1 = Employee('Barry', 45, 'FS', ['Python', 'JS'])  #Burada Barry ve 45 değişkenlerini Person class'ından miras aldık. Fs değişkenini Employee class'ından miras aldık. Python ve JS değişkenlerini Lang class'ından miras aldık. 
emp1.get_details()                                      #Employee class'ının get_details methodunu kullanıyoruz. override yaptığımız method
emp1.display_langs()                                    #Lang class'ının display_langs methodunu kullanıyoruz.

# person1 = Person('Aaron',37)
# person1.get_details()

print(Employee.mro())                                   #mro() methodu ile inheritance ının yapıldığı yerleri görebiliriz. Ne kadar class tan türetildi ise bu komut ile hepsini görebiliriz.

##! inner class

from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
