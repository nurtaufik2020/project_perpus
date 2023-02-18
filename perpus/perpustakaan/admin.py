from django.contrib import admin
#tambahan
from perpustakaan.models import Buku,Kelompok

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','kelompok_id','jumlah']
    search_fields =['judul','penulis','penerbit']
    list_filter = ('kelompok_id',)
    list_per_page = 4

# Register your models here.
admin.site.register(Buku,BukuAdmin )
admin.site.register(Kelompok)
