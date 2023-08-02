from django.contrib import admin
from .models import  Contact, Comentariu, Întrebări, Postări



@admin.register(Postări)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comentariu)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
    

@admin.register(Întrebări)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'email', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'email')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'
    
