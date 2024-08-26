from rest_framework import serializers
from .models import Expense, Deduction

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = '__all__'
