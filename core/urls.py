from core.views import BrigadeReportViewSet, PDFSubmissionViewSet, UnitViewSet, BrigadeViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

router = DefaultRouter()
router.register(r'submissions', PDFSubmissionViewSet)
router.register(r'reports', BrigadeReportViewSet)
router.register(r'units', UnitViewSet)
router.register(r'brigades', BrigadeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
