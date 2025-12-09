from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend      # <--- Import Filter
from rest_framework.filters import SearchFilter, OrderingFilter
from .forms import WargaForm, PengaduanForm

# ==========================================
# BAGIAN 1: VIEW UNTUK WEBSITE (HTML)
# (Jangan dihapus, karena warga/urls.py butuh ini)
# ==========================================

class WargaListView(ListView):
    model = Warga
    # template_name otomatis: warga/warga_list.html

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

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

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')


# ==========================================
# BAGIAN 2: VIEW UNTUK API (JSON)
# (Menggunakan ViewSet & Permissions)
# ==========================================

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Konfigurasi filter Warga (jika kamu sudah menambahkannya sebelumnya)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nik', 'nama_lengkap']
    search_fields = ['nama_lengkap', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

# --- 2. Update PengaduanViewSet ---
class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser] # Hanya Admin

    # Aktifkan fitur filter, search, dan ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filter Eksak (Pencarian Tepat) -> Contoh: ?status=BARU
    filterset_fields = ['status'] 
    
    # Pencarian Teks (Partial Search) -> Contoh: ?search=hilang
    search_fields = ['judul', 'deskripsi'] 
    
    # Pengurutan -> Contoh: ?ordering=-tanggal_lapor (Terbaru ke terlama)
    ordering_fields = ['status', 'tanggal_lapor']