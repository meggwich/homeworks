from django.contrib import admin

from .models import Article, Tag, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
