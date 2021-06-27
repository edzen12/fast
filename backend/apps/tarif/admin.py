from django.contrib import admin

from .models import DataTarif, Tarif


class DataTarifAdmin(admin.TabularInline):
    model = Tarif
    extra = 0


class TarifAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'data_tarif']
    save_on_top = True


class DataTarifAdmin(admin.ModelAdmin): 
    inlines = [DataTarifAdmin]  

admin.site.register(Tarif)
admin.site.register(DataTarif, DataTarifAdmin)