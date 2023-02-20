from django import forms

from exam.models import Course, Question


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'max_points']


class QuestionForm(forms.ModelForm):
    course_id = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label='Выберите название теста',
        to_field_name='id'
    )

    class Meta:
        model = Question
        fields = ['points', 'name', 'option_a', 'option_b', 'option_c', 'option_d', 'option_e', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
