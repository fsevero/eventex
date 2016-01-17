from django.contrib import admin
from django.utils.timezone import now

from attributetools import attribute

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at',
                    'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    @attribute(short_description='inscrito hoje?')
    @attribute(boolean=True)
    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    @attribute(short_description='Marcar como pago')
    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

admin.site.register(Subscription, SubscriptionModelAdmin)