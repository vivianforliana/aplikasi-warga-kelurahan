from django.contrib import admin
from .models import Warga, Pengaduan

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'alamat', 'no_telepon', 'tanggal_registrasi')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor')  # Tambahkan tanggal
    list_filter = ('status', 'tanggal_lapor')
    search_fields = ('judul', 'deskripsi', 'pelapor__nama_lengkap')
