from django.contrib import admin
from django.urls import path
#tambahan untuk membuat loginview
from django.contrib.auth.views import LoginView,LogoutView
#untuk meminta  view
# from perpustakaan.views import buku,penerbit,tambah_buku,ubah_buku
#bisa diganti dengan :
from perpustakaan.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name = 'buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku,name='ubah_buku'),
    #dikasih name agar jika ada perubahan pola alamat url kita tidak perlu mengubah alamat
    path('buku/hapus/<int:id_buku>', hapus_buku,name='hapus_buku'),
    #buat url untuk loginview
    path('masuk/',LoginView.as_view(),name='masuk'),
    path('keluar/',LogoutView.as_view(next_page='masuk'),name='keluar'),
    path('signup/', signup, name='signup'),
]
