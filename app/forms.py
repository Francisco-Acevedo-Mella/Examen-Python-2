from django import forms
from django.db.models import fields
from app.models import Job, User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','cpassword']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email' : 'email',
            'password': 'Contraseña',
            'cpassword': 'Confirmar Contraseña',
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'cpassword': forms.PasswordInput(attrs={'class': 'form-control'}),
            
        }
        


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Contraseña',
        }
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'desc','location']
        labels = {
            'title': 'Titulo',
            'desc': 'Descripcion',
            'location': 'Lugar',
            
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            
        }