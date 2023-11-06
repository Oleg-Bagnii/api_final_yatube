from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user'
    )

    class Meta:
        ordering = ('following',)

    def __str__(self):
        return f'follower - {self.user} following - {self.following}'


class Group(models.Model):
    title = models.CharField(verbose_name='Заголовок',
                             max_length=200)
    slug = models.SlugField(verbose_name='Идентификатор',
                            unique=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Заголовок')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        default_related_name = 'posts'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'
        ordering = ('-created',)

    def __str__(self):
        return self.text
