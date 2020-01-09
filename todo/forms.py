from django import forms
from .models import Context, List, Task

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
class ContextForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = '__all__'
        