from django.contrib import admin
from .models import Expense, Deduction

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'created_at')
    search_fields = ('description',)

@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'created_at')
    search_fields = ('description',)
