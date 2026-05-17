from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # ← была пропущена запятая
    path('', views.index, name='index'),
    path('api/ice-creams/', views.get_ice_creams_api, name='api_ice_creams'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)