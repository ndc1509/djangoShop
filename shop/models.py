from django.db import models

PRODUCT_STATUS = (
    ('C', 'Còn hàng'),
    ('H', 'Hết hàng'),
    ('CH', 'Chờ hàng'),
)


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

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

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')

    class Meta:
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.product.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(Product):
    publisher = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    size = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
