from django.db import models

from student.models import Student


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название теста')
    max_points = models.PositiveSmallIntegerField(verbose_name='Максимальное количество баллов')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f"{self.name} - {self.max_points}"


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Тест')
    points = models.PositiveSmallIntegerField(verbose_name='Количество баллов за правильный ответ')
    name = models.CharField(max_length=500, verbose_name='Содержание вопроса')
    option_a = models.CharField(max_length=200, verbose_name='Вариант ответа А')
    option_b = models.CharField(max_length=200, verbose_name='Вариант ответа B')
    option_c = models.CharField(max_length=200, verbose_name='Вариант ответа C')
    option_d = models.CharField(max_length=200, verbose_name='Вариант ответа D')
    option_e = models.CharField(max_length=200, verbose_name='Вариант ответа E')

    cat = (
        ('OptionA', 'OptionA'),
        ('OptionB', 'OptionB'),
        ('OptionC', 'OptionC'),
        ('OptionD', 'OptionD'),
        ('OptionE', 'OptionE')
    )

    answer = models.CharField(max_length=200, choices=cat, verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f"{self.course.name}: {self.name} - correct answer {self.answer}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Тест')
    points = models.PositiveSmallIntegerField(verbose_name='Количество баллов')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата сдачи теста')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f"{self.course.name}: {self.student.get_name} - {self.points} points"
