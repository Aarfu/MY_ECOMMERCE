from django.db import models

# Create your models here.
#model define our database(excel sheet withh columns name,phone,email,desc
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):#use to show database entry heading
        return self.name



