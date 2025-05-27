from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'input input-bordered w-full',
            'placeholder':'Taks title'
        })
    )
    
    desc = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'textarea w-full',
            'placeholder':'Taks desc'
        })
    )
    
    # status = forms.ChoiceField(choices=Task.TaskStatus.choices,required=False)
    status = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'select w-full'
        }), choices=Task.TaskStatus.choices)
    
    
    class Meta:
        model = Task
        fields=(
            'title', 'desc', 'status'
        )