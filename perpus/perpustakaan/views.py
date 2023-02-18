from django.shortcuts import render
from django.shortcuts import redirect
#tambahan ambil dari urls untuk ditampilkan
#AWAL
#from django.http import HttpResponse

# def buku(request):
#     return HttpResponse('Halaman Buku')

# def penerbit(request):
#     return HttpResponse('<h1>Halaman Penerbit</h1>')
#BARUUUUUU SETELAH BUAT TEMPLATES
#ORM
from perpustakaan.models import Buku    
#FORMS 
from perpustakaan.forms import FormBuku
# def buku(request):
#1.membuat subtitute variabel
    # judul=["Belajar Django", "Belajar Python","Belajar Bootstrap"]
    # penulis = "Nur Taufik"
    #2. buat dictionary untuk mengumpulkan data data variabel
    # konteks = {
    #     'title': judul,
    #     'penulis': penulis
    # }
from django.contrib import messages #ini tambahan untuk menambahkan pesan
# untuk menambahkan verifikasi harus login terlebih dahulu sebelum mengakses web
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url= settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Berhasil Dibuat")
            return redirect('signup')
        else:
            messages.error(request,"Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form=UserCreationForm()
        konteks={
            'form':form,
        }
    return render(request,'signup.html',konteks)


@login_required(login_url= settings.LOGIN_URL)
def ubah_buku(request,id_buku): #idbuku gunanya untuk get data yang akan diubah
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST,instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diperbaharui")
            return redirect('ubah_buku',id_buku=id_buku)
            #arahkan ke halaman ubah data (redirect)
            #return redirect('ubah_buku',id_buku=id_buku)
        
    else:
        form = FormBuku(instance=buku)
        konteks ={
            'forms':form ,
            'buku':buku,
        }
    return render(request,template,konteks)

#ini untuk menghapus data buku, pertama menggunakan get id bukunya
@login_required(login_url= settings.LOGIN_URL)
def hapus_buku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('buku')

#decorator untuk login, ini berhubungan dengan setting.py baris terakhir
@login_required(login_url= settings.LOGIN_URL)
def buku(request):
   # books = Buku.objects.all()
    # books = Buku.objects.filter(jumlah=1) itu akan menampilkan buku yang jumlahnya =1 

    #select * from Buku where jumlah = 90
    #inner join kelompok.id=buku.kelompok_id
    # where kelompok.nama ='produktif'
   # limit 3
    #books = Buku.objects.filter(kelompok_id__nama ="produktif") # ini inner join
    books = Buku.objects.all()

    konteks ={
        'books':books,
    }
    return render(request, 'buku.html', konteks)

@login_required(login_url= settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

#DASAR
# def tambah_buku(request):
#     form = FormBuku()
#     konteks = {
#         'forms':form,
#     }
#     return render(request,'tambah-buku.html', konteks)

@login_required(login_url= settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            #mengosongkan form kosong
            form = FormBuku()
            #menampilkan pesan
            pesan = "Data berhasil disimpan"
            konteks = {
                'forms':form,
                'pesans':pesan,
            }
            return render(request,'tambah-buku.html',konteks)
    else:
        form = FormBuku()
        konteks = {
            'forms':form,
        }
    return render(request,'tambah-buku.html', konteks)