from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


def slugification(title):
    base_slug = slugify(title)
    slug = base_slug
    count = 1
    while IceCream.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{count}"
        count += 1
        print(slug)
    return slug

class IceCream(models.Model):
    title = models.CharField(verbose_name='Мороженое', max_length=255)
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='static/images/%Y/%m/%d/', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=1)
    saves = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, )

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or IceCream.objects.filter(slug=self.slug).exists():
            self.slug = slugification(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('icecream', kwargs={'slug': self.slug})

    def get_description(self):
        return self.description[:150]


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Bag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    items = models.ManyToManyField('IceCream', related_name="icecreams")

    def __str__(self):
        return self.user.username
