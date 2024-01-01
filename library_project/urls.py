# library_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_app.views import  AdherentViewSet, LivreViewSet, AuteurViewSet, EmpruntViewSet

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'adherents', AdherentViewSet)
router.register(r'emprunts', EmpruntViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
