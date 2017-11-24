from django.contrib import admin

from .models import *


# Register your models here.

class YourAdmin(admin.ModelAdmin):
    readonly_fields = ('log_time',)


admin.site.register(KeywordLog, YourAdmin)
admin.site.register(HashLog)
