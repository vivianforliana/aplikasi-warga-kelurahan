from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanForm(forms.ModelForm):
    # Tambahkan field tanggal untuk input manual
    tanggal_registrasi = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Tanggal Pengaduan"
    )

    class Meta:
        model = Pengaduan
        fields = ['pelapor', 'judul', 'deskripsi', 'status', 'tanggal_registrasi']  # tambahkan tanggal
        widgets = {
            'deskripsi': forms.Textarea(attrs={'rows':4}),
        }
