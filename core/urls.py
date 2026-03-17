from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Cancha_Libre.views import JugadorViewSet, partidos_argentinos

router = DefaultRouter()
router.register(r'jugadores', JugadorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/partidos-ar/', partidos_argentinos),
]