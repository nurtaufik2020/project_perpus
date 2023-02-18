from django.forms import ModelForm
#---------------------------------
#import untuk membuat form
from django import forms

#---------------------------------


from perpustakaan.models import Buku



class FormBuku(ModelForm):  
    class Meta:
        model = Buku
        #exclude = ['judul', 'penulis', 'penerbit', 'jumlah', 'kelompok_id']
        #fields = '__all__'
        fields = ['judul', 'penulis', 'penerbit', 'jumlah', 'kelompok_id']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control','id':'inputJudul'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }
