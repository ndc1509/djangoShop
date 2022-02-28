from django.contrib import admin
from .models import *
from django.forms.models import BaseModelFormSet
from django import forms
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.object_id = object_id
        return super(CategoryAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_category":
            kwargs['queryset'] = Category.objects.exclude(pk=self.object_id)
        return super(CategoryAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book)
admin.site.register(ProductImage)
