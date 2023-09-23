from .models import Headphones,Manufact
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Headphones)
class HeadphonesAdmin(BaseAdmin):
    list_display = (
        'product_name',
        'description',
        'product_cost',
        'realise_date',
        'fabric',
    )
@admin.register(Manufact)
class ManufactAdmin(BaseAdmin):
    list_display = (
        'name_man',
    )

