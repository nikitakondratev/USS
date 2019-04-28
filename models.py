from django.db import models

# Create your models here.
class Post(models.Model):

    class Meta():
        db_table = 'post'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["create"]

    title = models.CharField("Заголовок", max_length=140)
    text = models.TextField("Текст статьи")
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Создано", auto_now_add=True)
    update = models.DateTimeField("Обновлено", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title
