# warga/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'warga', views.WargaViewSet)
router.register(r'pengaduan', views.PengaduanViewSet)

urlpatterns = [
    # GANTI 'api/' MENJADI '' (KOSONG)
    # Karena prefix 'api/' sudah diurus di data_kelurahan/urls.py
    path('', include(router.urls)), 
]