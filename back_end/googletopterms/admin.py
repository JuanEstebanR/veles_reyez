from django.contrib import admin
from .models import queries, comment


class QueriesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'rawQuery', 'relatedTo', 'public', 'user')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user')


# Register your models here.
admin.site.register(queries, QueriesAdmin)
admin.site.register(comment, CommentAdmin)
