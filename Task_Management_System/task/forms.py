from django import forms
from .models import TaskModel
from category.models import TaskCategory
class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=TaskCategory.objects.all())
    
    class Meta:
        model = TaskModel
        fields = '__all__'