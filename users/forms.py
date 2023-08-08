from django import forms

class LoginForms(forms.Form):
    user_name_l=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex: João Silva"
            }
        )
    )
    password=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite a sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    user_name_c=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex: João Silva"
            }
        )
    )
    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex: joaosilva@exemplo.com"
            }
        )
    )
    password=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite a sua senha"
            }
        )
    )
    password2=forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme a sua senha"
            }
        )
    )