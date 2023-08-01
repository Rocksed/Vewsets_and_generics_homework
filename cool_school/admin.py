from django.contrib import admin

from cool_school.models import Payment, Subscription


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']
