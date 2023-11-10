from django.db import models

class Task(models.Model):
    number_auto = models.CharField("Номер автомобиля", max_length=9)
    description = models.TextField('Описание нарушения')
    status_choises = (
        ('Не просмотрено','Не просмотрено'),
        ('Отклонено','Отклонено')
    )
    status = models.CharField('Статус', max_length=100, choices=status_choises, default="")

    def __str__(self):
        return self.number_auto

    class Meta:
        verbose_name = 'Нарушение'
        verbose_name_plural = 'Нарушения'

