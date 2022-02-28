from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from django.utils.safestring import mark_safe

PRODUCT_STATUS = (
    ('C', 'Còn hàng'),
    ('H', 'Hết hàng'),
    ('CH', 'Chờ hàng'),
)


# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    # total = models.IntegerField(min(0))
    stock = models.IntegerField()
    sold = models.IntegerField()
    status = models.CharField(choices=PRODUCT_STATUS, max_length=2)
    slug = models.SlugField()
    description = models.TextField()

    category = TreeManyToManyField(Category)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.product.name

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.image.url))
        else:
            return '(No image)'

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(Product):
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    size = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
