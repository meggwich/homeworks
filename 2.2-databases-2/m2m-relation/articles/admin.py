# articles/admin.py

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))
        if main_count == 0:
            raise ValidationError('Укажите основной раздел.')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел.')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

