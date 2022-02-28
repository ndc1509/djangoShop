from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple
from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.object_id = 0

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.object_id = object_id
        return super(CategoryAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def add_view(self, request, form_url='', extra_context=None):
        self.object_id = None
        return super(CategoryAdmin, self).add_view(
            request, form_url, extra_context=extra_context
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_id":
            kwargs['queryset'] = Category.objects.exclude(pk=self.object_id)
        return super(CategoryAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    readonly_fields = ('image_preview',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    formfield_overrides = {
        TreeManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Book, ProductAdmin)
admin.site.register(Author)
