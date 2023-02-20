from django.db import models

from student.models import Student


class Course(models.Model):
    name = models.CharField(max_length=30)
    max_points = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.max_points}"


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=500)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    option_e = models.CharField(max_length=200)

    cat = (
        ('OptionA', 'OptionA'),
        ('OptionB', 'OptionB'),
        ('OptionC', 'OptionC'),
        ('OptionD', 'OptionD'),
        ('OptionE', 'OptionE')
    )

    answer = models.CharField(max_length=200, choices=cat)

    def __str__(self):
        return f"{self.course.name}: {self.name} - correct answer {self.answer}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.name}: {self.student.get_name} - {self.points} points"
