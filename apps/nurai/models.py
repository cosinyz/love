from django.db import models


class Student(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.IntegerField("Возраст")
    city = models.CharField("Город", max_length=100)
    email = models.EmailField("Email")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name
