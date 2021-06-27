from django.contrib import admin
from apps.contact.models import FormEmail


class FormEmailAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'number')
    list_filter = ('fullname', 'number')
    search_fields = ('fullname',)


admin.site.register(FormEmail, FormEmailAdmin)