from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView # Tambahkan CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm # Impor form yang baru dibuat

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):  # halaman daftar semua pengaduan
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'  # template baru

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list') 
