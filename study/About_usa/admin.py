from django.contrib import admin
from About_usa.models import Techarc

# Register your models here.
class TecharcAdmin(admin.ModelAdmin):
    list_display=('id','tid','tname','temail')

admin.site.register(Techarc,TecharcAdmin)
