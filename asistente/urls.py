from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'eventos', views.EventoView, basename='eventos')
urlpatterns = [
    path("api/", include(router.urls)),
    # path("documentacion/", include_docs_urls(title="Asistente"))
]