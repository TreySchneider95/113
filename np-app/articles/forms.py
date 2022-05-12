from django import forms
from .models import Article

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.Select(attrs={'class' : 'form-control form-select'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
            'section': forms.Select(attrs={'class' : 'form-control form-select'}),
        }