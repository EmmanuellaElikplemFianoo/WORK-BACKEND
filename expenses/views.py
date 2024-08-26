from rest_framework import viewsets
from .models import Expense, Deduction
from .serializers import ExpenseSerializer, DeductionSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DeductionViewSet(viewsets.ModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer
