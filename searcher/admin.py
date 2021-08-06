from django.contrib import admin
from searcher.models import Info
# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    search_fields = ("ten", "link_sp")
