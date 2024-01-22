from django.db import models

class SupplierRegistration(models.Model):
     Supplier_name = models.CharField(max_length=50)
     owner_name = models.CharField(max_length=30)
     address = models.CharField(max_length=30)
     phone_number = models.CharField(max_length=12)
     quotation = models.FileField(upload_to='doc/')


     def __str__(self):
          return f'Supplier name: {self.Supplier_name}\n\t,   phone number :{self.phone_number}\n'

     class Meta:
          verbose_name_plural = "ספקים"