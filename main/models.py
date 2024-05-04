from django.db import models
from django.utils import timezone
from rest_framework.reverse import reverse


class Survey(models.Model):
    title = models.CharField('Название', max_length=100)
    name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    city = models.CharField('Город', max_length=20)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField('Название', max_length=100)
    name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    city = models.CharField('Город', max_length=20)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.city}"

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.title
