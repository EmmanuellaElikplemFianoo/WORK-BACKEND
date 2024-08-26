from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, DeductionViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'deductions', DeductionViewSet)  # Add DeductionViewSet

urlpatterns = [
    path('', include(router.urls)),
]
