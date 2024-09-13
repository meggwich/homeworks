from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=20)
    articles = models.ManyToMany(
        Article,
        through='Scope',
        through_fields=('article', 'teg'),
    )

class Relationship(models.Model):
    group = models.ForeignKey(Article, on_delete=models.CASCADE)
    person = models.ForeignKey(Tag, on_delete=models.CASCADE)
    scoper = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="relation_scope",
    )
    tag_name = models.CharField(max_length=20)

