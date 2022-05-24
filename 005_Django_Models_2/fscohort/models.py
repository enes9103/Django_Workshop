from django.db import models

class Student(models.Model):                                    #models'ten inherit ediyoruz
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senior'),
        ("GRD", 'Graduate'),
    ]
    first_name = models.CharField(max_length=50)                 #field name, field type, field options Django documentationdan model içindeki field types field options incelenebilir.
    last_name = models.CharField(max_length=50)                  #CharField -> string field
    number = models.IntegerField()                               #IntegerField -> integer field
    about = models.TextField(null=True, blank=True)              #TextField -> text field  blank=True -> bu alana veri girilmeyebilir.
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')   #upload_to -> upload_to parametresi ile upload edilen resimlerin nereye gönderileceği belirlenir.
                                                                            #image field kullanacaksak python görüntlenme paketi olan pillow yüklenmelidir.
                                                                            #python -m pip install Pillow
    register_date = models.DateTimeField(auto_now_add=True)     #DateTimeField -> date time field
    update_date = models.DateTimeField(auto_now=True)           #auto_now -> update_date fieldının her değiştirilmesi zamanında otomatik olarak güncellenir.
    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default="FR") #choices -> choices parametresi ile field için kullanılabilir bir liste belirlenir.
    
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"          #adminde tabloya eklenen verilerin admin panelinde görünmesi için __str__ fonksiyonu kullanılır.

    class Meta:                                                 #admin panelinde tabloların isimleri veya başlıklarını değiştirmek, sıralama ölçütü gibi işlemleri class Meta kullanılır.
        ordering = ["number"]                                   #admin panelinde verilerin sıralanması için ordering kullanılır.
        verbose_name_plural = "Öğrenciler"                      #Django dokumentasyon Models içinden Meta options incelenebilir.