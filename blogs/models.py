from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок блоговой записи")
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое", blank=True, null=True)
    image = models.ImageField(
        upload_to="blogs/media",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Добавьте изображение",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(verbose_name="Признак публикации", help_text="Установите признак "
                                                                                        "публикации")
    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )


    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title

