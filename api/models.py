import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Genre(models.Model):
    name = models.CharField(
        'Название жанра',
        max_length=100,
        unique=True,
        db_index=True,
        help_text='Введите название жанра'
    )
    slug = models.SlugField(
        'Краткое название жанра (англ.)',
        max_length=50,
        unique=True,
        help_text='Введите краткое название жанра (англ.)'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name[0:35]


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=100,
        unique=True,
        db_index=True,
        help_text='Введите название категории'
    )
    slug = models.SlugField(
        'Краткое название категории (англ.)',
        max_length=50,
        unique=True,
        help_text='Введите краткое название категории (англ.)'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name[0:35]


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=350,
        unique=True,
        db_index=True,
        help_text='Введите название произведения'
    )
    year = models.PositiveSmallIntegerField(
        'Год выпуска',
        null=True,
        blank=True,
        default=None,
        db_index=True,
        validators=[MaxValueValidator(datetime.date.today().year), ],
        help_text='Введите год выпуска произведения'
    )
    description = models.TextField(
        'Описание произведения',
        max_length=400,
        null=True,
        blank=True,
        help_text='Введите описание произведения'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        db_index=True,
        help_text='Выберите жанр произведения'
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL,
        help_text='Выберите категорию произведения'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name[0:50]


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Название произведения',
    )
    text = models.TextField(
        'Отзыв на произведение',
        help_text='Поле для отзыва',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[MaxValueValidator(10), MinValueValidator(1)],
        help_text='Поставь оценку',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    def __str__(self):
        title = self.title
        author = self.author
        text = self.text[:15]
        return f'{title}-{author}-{text}'

    class Meta:
        ordering = ['-pub_date']
        unique_together = ['title', 'author']


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Название',
    )
    text = models.TextField(
        'Текст',
        help_text='Поле для коментария',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    def __str__(self):
        author = self.author
        text = self.text[:15]
        return f'{author}-{text}'

    class Meta:
        ordering = ['-pub_date']
