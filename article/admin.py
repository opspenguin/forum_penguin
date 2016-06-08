from django.contrib import admin
from models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","status","owner","block","create_timestamp","last_update_timestamp")
    search_fields = ["title","status","content"]
    list_filter = ("block",)

#admin.register(Article)
admin.register(Article,ArticleAdmin)