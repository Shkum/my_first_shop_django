from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email']
    # ordering = ['-id']
    ordering = ['id']
    list_display = [field.name for field in Subscriber._meta.fields]
    # exclude = []  # to hide fields in the admin page
    # fields = []  # to show only fields in the admin page
    list_filter = ['name']  # add column for quick filtering
    search_fields = ['name']  # add search field to django admin

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
