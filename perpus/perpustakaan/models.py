from django.db import models

#membuat foreign key
class Kelompok(models.Model):
    nama= models.CharField(max_length=9)
    keterangan = models.TextField()
#lalu tambahkan foreign key di class buku
    
    def __str__(self):
        return self.nama
# Create your models here.

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    jumlah = models.IntegerField(null=True)
    #Tambahan foreign key
    kelompok_id = models.ForeignKey (Kelompok,on_delete = models.CASCADE ,null =True)
    
    def __str__(self):
        return self.judul 
        
    #setelah dibuat silahkan migrasi database
    #python manage.py makemigrations
    #python manage.py migrate
    #hasilnya perpustakaan_buku

