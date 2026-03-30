from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Topic
from .models import Company


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'target_company', 'password1', 'password2']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'difficulty', 'status', 'notes', 'problem_link']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
            'problem_link': forms.URLInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'role', 'preparation_status', 'interview_date']

        
