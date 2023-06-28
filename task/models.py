from django.db import models

from django.db import models
from django.utils import timezone

class Task(models.Model):
    """
    Модель для представления задачи.

    Attributes:
        STATUS_CHOICES (tuple): Варианты статусов задачи.
        description (TextField): Описание задачи.
        status (CharField): Статус задачи.
        created_at (DateTimeField): Дата создания задачи.
        updated_at (DateTimeField): Дата обновления задачи.
    """
    STATUS_CHOICES = (
        ('completed', 'Выполнено'),
        ('not_completed', 'Не выполнено'),
    )

    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_completed', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        """
        Возвращает строковое представление задачи (описание).

        Returns:
            str: Строковое представление задачи.
        """
        return self.description
