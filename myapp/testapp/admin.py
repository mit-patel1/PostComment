from django.contrib import admin
from testapp.models import Comment, Post, Like

# Register your models here.
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('*')    


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)