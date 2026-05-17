from django.db import models


class IceCream(models.Model):
    title = models.CharField(  # Исправьте tittle на title
        max_length=50,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    photo = models.ImageField(
        upload_to='ice_creams/',  # Лучше использовать отдельную папку
        verbose_name='Фото'
    )

    # Добавьте поля для категорий
    FLAVOR_TYPES = [
        ('gelato', 'Джелато'),
        ('icecream', 'Мороженое'),
        ('sorbet', 'Сорбет'),
    ]

    flavor_type = models.CharField(
        max_length=20,
        choices=FLAVOR_TYPES,
        default='icecream',
        verbose_name='Тип'
    )

    is_popular = models.BooleanField(
        default=False,
        verbose_name='Популярное'
    )

    is_seasonal = models.BooleanField(
        default=False,
        verbose_name='Сезонное'
    )

    is_new = models.BooleanField(
        default=False,
        verbose_name='Новинка'
    )

    is_vegan = models.BooleanField(
        default=False,
        verbose_name='Веганское'
    )

    season = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ('spring', 'Весна'),
            ('summer', 'Лето'),
            ('autumn', 'Осень'),
            ('winter', 'Зима'),
        ],
        verbose_name='Сезон'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'