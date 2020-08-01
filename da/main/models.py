from django.db import models


class Text(models.Model):
    title = models.CharField('Title', max_length=20)
    text = models.TextField('Text')
    comment = models.TextField('Comment')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Texts"