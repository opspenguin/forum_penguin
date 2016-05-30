from django.contrib import admin
from models import Blocks
# Register your models here.
class BlocksAdmin(admin.ModelAdmin):
    list_display = ("name","desc","manager","create_timestamp","last_update_timestamp")

admin.site.register(Blocks,BlocksAdmin)
