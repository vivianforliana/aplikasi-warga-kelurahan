from django.urls import path
from . import views

urlpatterns = [
    # Daftar Warga (Halaman Utama aplikasi warga)
    path('', views.WargaListView.as_view(), name='warga-list'),
    
    # Detail, Tambah, Edit, Hapus Warga
    path('', views.WargaListView.as_view(), name='warga-list'),
    path('baru/', views.WargaCreateView.as_view(), name='warga-create'),
    path('<int:pk>/edit/', views.WargaUpdateView.as_view(), name='warga-update'),
    path('<int:pk>/hapus/', views.WargaDeleteView.as_view(), name='warga-delete'),

    # Pengaduan
    path('pengaduan/', views.PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/baru/', views.PengaduanCreateView.as_view(), name='pengaduan-create'),
    path('pengaduan/<int:pk>/edit/', views.PengaduanUpdateView.as_view(), name='pengaduan-update'),
    path('pengaduan/<int:pk>/hapus/', views.PengaduanDeleteView.as_view(), name='pengaduan-delete'),
]